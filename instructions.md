# Blog Management Instructions

This blog has been converted from WordPress to Hugo using the `terminal` theme.

## 1. Serving the site locally

To preview your blog locally with live-reloading:

1.  **Navigate to the blog directory:**
    ```bash
    cd keithrozario_blog
    ```
2.  **Start the Hugo server:**
    ```bash
    hugo server
    ```
    *Note: If `hugo` is not installed on your system, you can download it from the [Hugo GitHub Releases](https://github.com/gohugoio/hugo/releases).*

3.  **View the site:**
    Open your browser and go to `http://localhost:1313`.

## 2. Adding a new post

1.  **Create the post file:**
    From inside the `keithrozario_blog` directory, run:
    ```bash
    hugo new posts/my-new-post.md
    ```
2.  **Edit the content:**
    Open `content/posts/my-new-post.md` in your favorite editor.
3.  **Update Front Matter:**
    The top of the file contains "Front Matter" in TOML format. Ensure it looks like this:
    ```toml
    +++
    title = "My New Post"
    date = "2026-02-14T12:00:00Z"
    draft = false
    tags = ["example", "hugo"]
    categories = ["General"]
    +++
    ```
4.  **Add your content:**
    Write your post using standard Markdown below the second `+++`.

## 3. Managing Images

*   **Uploads Location:** All images are stored in `assets/uploads/`. This allows Hugo to process them using Hugo Pipes (resizing, optimizing).
*   **Adding New Images:** Place any new images in `assets/uploads/`.
*   **Referencing Images:** Use standard Markdown syntax. Do NOT use HTML tags (like `<figure>` or `<div>`) around images, as this prevents Hugo from processing them:
    ```markdown
    ![Alt text](/uploads/your-image.png)
    ```
*   **Responsive Resizing:** 
    - The blog uses a custom image render hook (`layouts/_default/_markup/render-image.html`).
    - If an image width is greater than 1024px, Hugo automatically generates a `srcset` with multiple sizes (480w, 768w, 1024w) for responsive loading.
    - Images are lazily loaded by default for performance.

## 4. Building for Production

To generate the final static files (found in the `public/` folder):
```bash
cd keithrozario_blog
hugo
```
