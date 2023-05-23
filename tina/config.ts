import { defineConfig } from "tinacms";

// Your hosting provider likely exposes this as an environment variable
const branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "master";

export default defineConfig({
  branch,
  clientId: process.env.TINA_CLIENTID!, // Get this from tina.io
  token: process.env.TINA_TOKEN!, // Get this from tina.io

  build: {
    outputFolder: "admin",
    publicFolder: "static",
  },
  media: {
    tina: {
      mediaRoot: "",
      publicFolder: "static",
    },
  },
  schema: {
    collections: [
      {
        name: "articles",
        label: "Articles",
        path: "content",
        fields: [
          {
            type: "string",
            name: "title",
            label: "Title",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "authors",
            label: "Authors",
            list: true,
          },
          {
            type: "datetime",
            name: "date",
            label: "Date",
            ui: {
              dateFormat: "YYYY-MM-DD"
            },
            description: "Date the article appeared in print",
          },
          {
            type: "string",
            name: "categories",
            label: "Categories",
            list: true,
            options: [
              "Campus",
              "Off-Campus",
              "Culture",
              "Opinion",
              "Art",
              "Sports",
              "Humor",
              "World",
              "Editorial",
              "Puzzles",
              "Science & Tech",
              "Student Life",
              "Academics",
            ],
            ui: {
              direction: "horizontal"
            },
            description: "Choose one or two categories. If you're not sure, ask the editor-in-chief.",
          },  
          {
            type: "string",
            name: "tags",
            label: "Tags",
            list: true,
            options: [
              "Vol. CXXVI, Issue 1",
              "Vol. CXXVI, Issue 2",
              "Vol. CXXVI, Issue 3",
              "Vol. CXXVI, Issue 4",
              "Vol. CXXVI, Issue 5",
            ],
            ui: {
              component: "select"
            }
          },
          {
            type: "number",
            name: "weight",
            label: "Weight",
            description: "Negative numbers will appear at the top of the front page. Fine to leave at 0 unless it's a special post.",
          },
          {
            type: "boolean",
            name: "show_thumbnail",
            label: "Show Thumbnail",
            description: "whether to show the thumbnail image at the top of the post. it will fill the width of the screen, and you'll have to scroll to get to the rest of the post. often better to leave this off and add the image to the body of the post.",
          },
          {
            type: "image",
            name: "thumbnail",
            label: "Thumbnail",
          },
          {
            type: "image",
            name: "images",
            label: "Opengraph Preview",
            list: true,
            description: "This will appear when you post a link to the article on social media. Fine to just use the thumbnail (need to reselect it).",
          },
          {
            type: "string",
            name: "sidebar",
            label: "Sidebar",
            options: [
              "left",
              "right",
              "false",
            ],
            description: "whether to show the sidebar, and if so, which side. (on mobile it will always be at the bottom.) it shows other recent articles, so leave on unless it's an art feature or something that you want to have the whole screen width.",
            ui: {
              component: "radio-group",
              direction: "horizontal",
              variant: "button",
            }
          },
          {
            type: "boolean",
            name: "toc",
            label: "Table of Contents",
            description: "if you have any markdown headings ≥ #3 in the body of the post, this will generate a table of contents for them.",
          },
          {
            type: "string",
            name: "widgets",
            label: "Widgets",
            list: true,
            description: "(leave as default probably)",
            options: [
              "recent",
              "categories",
              "taglist",
              "write-for-the-tech",
              "featured"
            ],
            ui: {
              direction: "horizontal"
            }
          },
          {
            type: "string",
            name: "summary",
            label: "Summary Preview",
            description: "This will appear on the front page. It should be a sentence or two, and it can have markdown components like links. The first sentence of the article is usually good.",
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body",
            isBody: true,
          },
        ],
        defaultItem: () => ({
          title: "New Article",
          authors: [],
          date: new Date(),
          categories: [],
          tags: ["Vol. CXXVI, Issue 5"],
          weight: 0,
          thumbnail: "/default3.jpg",
          show_thumbnail: true,
          sidebar: "right",
          toc: true,
          widgets: ["recent", "categories", "taglist", "write-for-the-tech"],
          summary: "",
          images: ["/default3.jpg"],
          body: "",
        }),
      },
    ],
  },
});