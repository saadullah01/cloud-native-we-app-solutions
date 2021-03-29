import * as functions from "firebase-functions";
import got from "got";

interface IBlogPost {
  title: string;
  content: string;
}

const publishToDevto = (blogPost: IBlogPost) => got.post("https://dev.to/api/articles", {
  headers: {
    "api-key": functions.config().crossposttodevto.apikey
  },
  json: {
    article: {
      title: blogPost.title,
      body_markdown: blogPost.content,
      published: false
    }
  }
});

export default functions.firestore
  .document("posts/{slug}")
  .onCreate(
    async (
      snapshot: functions.firestore.DocumentSnapshot,
      context: functions.EventContext
    ) => {
      const blogPost = snapshot.data() as IBlogPost || {};
      console.log(
        `Posting to dev.to... Slug: ${
        context.params.slug
        }. Post: ${JSON.stringify(blogPost)}`
      );

      try {
        await publishToDevto(blogPost);
        console.log("Blog post successfully posted to dev.to.");
      } catch (error) {
        console.error(error);
      }
    }
  );
