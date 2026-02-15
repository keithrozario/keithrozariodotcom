# Blog Management Instructions

This blog has been converted from WordPress to Hugo using the `terminal` theme. The source code is hosted on GitHub, and deployment is handled automatically via GitHub Actions.

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
    *Tip: The URL will automatically be generated as `/year/month/slug/` based on the date and title. You can override the slug by adding `slug = "my-custom-url"` to the front matter.*

4.  **Add your content:**
    Write your post using standard Markdown below the second `+++`.

## 3. Managing Images

*   **Location:** All images MUST be stored in `keithrozario_blog/assets/uploads/`.
    *   *Why?* Placing images here allows Hugo to process them (resize, optimize) using Hugo Pipes.
*   **Adding New Images:** Simply copy your image files (e.g., `my-image.png`) into `keithrozario_blog/assets/uploads/`.
*   **Referencing Images:** Use standard Markdown syntax. **Do NOT use HTML tags** (like `<figure>` or `<div>`) around images, as this prevents Hugo from processing them:
    ```markdown
    ![Alt text](/uploads/my-image.png)
    ```
*   **Responsive Behavior:** 
    - The site uses a custom render hook (`layouts/_default/_markup/render-image.html`).
    - Large images (>1024px width) are automatically resized to multiple widths (480px, 768px, 1024px) and served with `srcset` for faster loading on mobile devices.
    - Images are lazy-loaded by default.

## 4. Publishing Changes

You do **not** need to manually build the site. GitHub Actions will automatically build and deploy your changes when you push to the `main` branch.

1.  **Stage your changes:**
    ```bash
    git add .
    ```
2.  **Commit your changes:**
    ```bash
    git commit -m "Add new post: My New Post"
    ```
3.  **Push to GitHub:**
    ```bash
    git push origin main
    ```

4.  **Wait for Deployment:**
    - Go to the "Actions" tab in your GitHub repository to see the deployment progress.
    - Once the workflow completes (usually 1-2 minutes), your changes will be live at `https://keithrozario.com`.
