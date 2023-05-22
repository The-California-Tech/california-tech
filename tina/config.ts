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
              component: "tags"
            }
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
          },
          {
            type: "image",
            name: "thumbnail",
            label: "Thumbnail",
          },
          {
            type: "boolean",
            name: "show_thumbnail",
            label: "Show Thumbnail",
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
            ui: {
              component: "select"
            }
          },
          {
            type: "boolean",
            name: "toc",
            label: "Table of Contents",
          },
          {
            type: "string",
            name: "widgets",
            label: "Widgets",
            list: true,
            options: [
              "recent",
              "categories",
              "taglist",
              "write-for-the-tech",
              "featured"
            ],
          },
          {
            type: "string",
            name: "summary",
            label: "Summary Preview",
          },
          {
            type: "image",
            name: "images",
            label: "Opengraph Preview",
            list: true,
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
          tags: [],
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