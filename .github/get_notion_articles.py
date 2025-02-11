import os
import logging
from notion_client import Client
from datetime import datetime
import yaml
import re
import requests
from pathlib import Path
from slugify import slugify

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('notion_export.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class NotionExporter:
    def __init__(self, token, image_dir="/img"):
        self.notion = Client(auth=token)
        self.image_dir = image_dir
        
    def download_image(self, url, filename):
        """Download image from Notion and save it to the specified directory"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Create directory if it doesn't exist
            full_path = os.path.join(self.image_dir, filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            with open(full_path, 'wb') as f:
                f.write(response.content)
            
            return full_path
        except Exception as e:
            logger.error(f"Failed to download image {url}: {str(e)}")
            return None

    def get_articles_from_database(self, database_id):
        """
        Fetch articles that are Ready to Print and from the latest issue
        """
        try:
            response = self.notion.databases.query(
                database_id=database_id,
                filter={
                    "and": [
                        {
                            "property": "Status",
                            "status": {  # Changed from select to status
                                "equals": "Ready to Print"
                            }
                        },
                        {
                            "property": "Issue",
                            "select": {
                                "equals": "18 February 2025"
                            }
                        }
                    ]
                }
            )
            return response["results"]
        except Exception as e:
            logger.error(f"Failed to query database: {str(e)}")
            return []

    def convert_block_to_markdown(self, block):
        """Convert a single Notion block to Markdown"""
        block_type = block["type"]
        
        try:
            if block_type == "paragraph":
                return self._handle_paragraph(block)
            elif block_type == "heading_1":
                return f"# {self._get_text_content(block['heading_1'])}\n\n"
            elif block_type == "heading_2":
                return f"## {self._get_text_content(block['heading_2'])}\n\n"
            elif block_type == "heading_3":
                return f"### {self._get_text_content(block['heading_3'])}\n\n"
            elif block_type == "bulleted_list_item":
                return f"* {self._get_text_content(block['bulleted_list_item'])}\n"
            elif block_type == "numbered_list_item":
                return f"1. {self._get_text_content(block['numbered_list_item'])}\n"
            elif block_type == "image":
                return self._handle_image(block)
            elif block_type == "quote":
                return f"> {self._get_text_content(block['quote'])}\n\n"
            else:
                logger.warning(f"Unhandled block type: {block_type}")
                return ""
        except Exception as e:
            logger.error(f"Error converting block {block['id']}: {str(e)}")
            return ""

    def _handle_paragraph(self, block):
        text = self._get_text_content(block['paragraph'])
        return f"{text}\n\n" if text else "\n"

    def _handle_image(self, block):
        try:
            image = block["image"]
            if image["type"] == "external":
                url = image["external"]["url"]
            else:
                url = image["file"]["url"]

            caption = ""
            if image.get("caption"):
                caption = self._get_text_content({"rich_text": image["caption"]})

            # Generate filename based on date and some unique identifier
            date_str = datetime.now().strftime("%Y/%b").lower()
            filename = f"{date_str}/{slugify(caption or 'image')}.png"
            
            # Download and save the image
            saved_path = self.download_image(url, filename)
            if saved_path:
                return f"![{caption}]({saved_path})\n\n"
            return ""
        except Exception as e:
            logger.error(f"Error handling image block: {str(e)}")
            return ""

    def _get_text_content(self, block_content):
        """Extract text content from a block, handling rich text formatting"""
        if not block_content.get("rich_text"):
            return ""
        
        text = ""
        for rt in block_content["rich_text"]:
            content = rt["plain_text"]
            if rt.get("annotations"):
                if rt["annotations"]["bold"]:
                    content = f"**{content}**"
                if rt["annotations"]["italic"]:
                    content = f"*{content}*"
                if rt["annotations"]["strikethrough"]:
                    content = f"~~{content}~~"
                if rt["annotations"]["code"]:
                    content = f"`{content}`"
            text += content
        return text

    def generate_frontmatter(self, page):
        """Generate YAML frontmatter from page properties"""
        try:
            properties = page["properties"]
            
            # Basic frontmatter
            frontmatter = {
                "title": properties["Name"]["title"][0]["plain_text"],
                # Handle "Assigned to" as rich_text
                "authors": [properties["Assigned to"]["rich_text"][0]["plain_text"]] if properties["Assigned to"]["rich_text"] else [],
                "categories": [],
                "tags": [],
                "weight": 0,
                "sidebar": "right",
                "toc": False,
                "widgets": [
                    "write-for-the-tech",
                    "editorial",
                    "taglist",
                    "categories",
                    "recent"
                ]
            }

            # Handle Issue date (from select field)
            if "Issue" in properties and properties["Issue"]["select"]:
                try:
                    issue_text = properties["Issue"]["select"]["name"]  # "18 February 2025"
                    issue_date = datetime.strptime(issue_text, "%d %B %Y")
                    frontmatter["date"] = issue_date.strftime("%Y-%m-%d %H:%M:%S -0700")
                except Exception as e:
                    logger.warning(f"Could not parse Issue date: {e}")
                    # Fallback to current date
                    frontmatter["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S -0700")
            else:
                frontmatter["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S -0700")

            # Handle Tags
            if "Tags" in properties and properties["Tags"]["multi_select"]:
                tags = properties["Tags"]["multi_select"]
                for tag in tags:
                    if tag["name"] == "Column":
                        frontmatter["categories"].append("The Inside World")
                    frontmatter["tags"].append(tag["name"])

            # Handle Info field
            if "Info" in properties and properties["Info"]["rich_text"]:
                info = properties["Info"]["rich_text"][0]["plain_text"]
                frontmatter["summary"] = info

            return yaml.dump(frontmatter, sort_keys=False, allow_unicode=True)
        except Exception as e:
            logger.error(f"Error generating frontmatter: {str(e)}")
            return ""

    def convert_block_to_markdown(self, block):
        """Convert a single Notion block to Markdown"""
        block_type = block["type"]
        
        try:
            if block_type == "paragraph":
                return self._handle_paragraph(block)
            elif block_type == "heading_1":
                return f"# {self._get_text_content(block['heading_1'])}\n\n"
            elif block_type == "heading_2":
                return f"## {self._get_text_content(block['heading_2'])}\n\n"
            elif block_type == "heading_3":
                return f"### {self._get_text_content(block['heading_3'])}\n\n"
            elif block_type == "bulleted_list_item":
                return f"* {self._get_text_content(block['bulleted_list_item'])}\n"
            elif block_type == "numbered_list_item":
                return f"1. {self._get_text_content(block['numbered_list_item'])}\n"
            elif block_type == "image":
                return self._handle_image(block)
            elif block_type == "quote":
                return f"> {self._get_text_content(block['quote'])}\n\n"
            elif block_type == "link_preview":
                # Handle link previews - we'll just extract the URL
                url = block["link_preview"]["url"]
                return f"<{url}>\n\n"
            else:
                logger.warning(f"Unhandled block type: {block_type}")
                return ""
        except Exception as e:
            logger.error(f"Error converting block {block['id']}: {str(e)}")
            return ""


    def export_page(self, page_id):
        """Export a single Notion page to Markdown"""
        try:
            # Get page
            page = self.notion.pages.retrieve(page_id)
            
            # Generate frontmatter
            content = f"---\n{self.generate_frontmatter(page)}---\n\n"
            
            # Get all blocks
            blocks = self.notion.blocks.children.list(page_id)
            
            # Convert blocks to markdown
            for block in blocks["results"]:
                content += self.convert_block_to_markdown(block)
            
            return content
        except Exception as e:
            logger.error(f"Error exporting page {page_id}: {str(e)}")
            return None

def main():
    try:
        # Get environment variables
        token = os.environ.get("NOTION_TOKEN")
        if not token:
            raise ValueError("NOTION_TOKEN environment variable not set")

        database_id = os.environ.get("NOTION_DATABASE_ID")
        if not database_id:
            raise ValueError("NOTION_DATABASE_ID environment variable not set")

        # Create output directory if it doesn't exist
        output_dir = "content/posts"
        os.makedirs(output_dir, exist_ok=True)

        # Initialize exporter
        exporter = NotionExporter(token)
        
        # Get articles from database
        articles = exporter.get_articles_from_database(database_id)
        
        if not articles:
            logger.info("No articles found ready to print for the current issue")
            return

        # Export each article
        for page in articles:
            try:
                content = exporter.export_page(page["id"])
                if content:
                    title = page["properties"]["Name"]["title"][0]["plain_text"]
                    filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slugify(title)}.md"
                    filepath = os.path.join(output_dir, filename)
                    
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    
                    logger.info(f"Successfully exported {filename}")
            except Exception as e:
                logger.error(f"Failed to export page {page['id']}: {str(e)}")

    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")

if __name__ == "__main__":
    main()
