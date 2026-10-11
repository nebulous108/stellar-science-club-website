# Stellar Science Club

The official website for **Stellar Science Club**, an Australia-focused science community on Discord with 200+ members. The club brings together students interested in science, mathematics, technology and engineering through collaborative learning, homework help, study sessions and discussions about new discoveries.

🌐 **Website:** [https://nebulous108.github.io/stellar-science-club-website/](https://nebulous108.github.io/stellar-science-club-website/)
💬 **Discord:** [https://dsc.gg/stellar-science-club](https://dsc.gg/stellar-science-club)
▶️ **YouTube:** [https://www.youtube.com/@StellarScienceClub](https://www.youtube.com/@StellarScienceClub)

---

## About the Project

The Stellar Science Club website serves as the central public-facing hub for the community. It introduces visitors to the club, explains what members can participate in, showcases the server's structure and provides information about its educational resources and activities.

The project is built as a static, multi-page website using HTML, with GitHub Pages for hosting and GitHub actions for autonmated tasks, such as currently updating the videos list from YouTube.

The main goals of the project are to:

- Make the community easier for new members to discover.
- Present the server's channels, features and activities in an organised way.
- Provide dedicated information for students preparing for John Monash Science School (JMSS).
- Promote the club's educational YouTube content.
- Keep the website's video listings updated automatically without manually editing the page after every upload.

## Website Pages

### 1. Home — `index.html`

The homepage introduces Stellar Science Club and its purpose. It acts as the main entry point for visitors, highlighting the community and directing them towards the other sections of the website. 

### 2. Features — `features.html`

This page provides an overview of what the server offers, including:

- Homework help and collaborative learning.
- Science discussions and interesting discoveries.
- Study sessions and Kahoot battles.
- JMSS preparation resources.
- Educational videos published on YouTube.

It helps visitors understand the different ways they can participate in the community.

### 3. Study & Events — `study-events.html`

This page explains the club's learning activities and community events, including study sessions and Kahoot battles.

Study-session content is also published on the Stellar Science Club YouTube channel, allowing students to revisit educational material and access it outside live sessions.

### 4. Community — `community.html`

The Community page provides a visual directory of the Discord server's channel categories.

It helps visitors understand how the server is organised, from general community spaces to specialised educational channels, and makes it easier to find areas relevant to their interests.

### 5. JMSS Preparation — `jmss.html`

This page highlights the specialised channels available to students preparing for John Monash Science School.

These include dedicated spaces for:

- JMSS interview preparation.
- Year 10 entry preparation.
- Year 11 entry preparation.
- Exam advice and related discussions.

The aim is to make it easier for students to find relevant preparation resources and learn alongside others working towards similar goals.

### 6. YouTube — `youtube.html`

The YouTube page showcases educational videos published on the Stellar Science Club channel. Rather than relying entirely on a manually maintained list, the page reads video information from `data/videos.json`.

The listing includes available video information such as titles, thumbnails, publication dates and links to watch the videos.

The page is connected to an automated workflow that refreshes the underlying JSON data, helping the website stay current as new videos are published.

### 7. Team — `team.html`

The Team page introduces the people responsible for running the community, including the founder, co-founder and administration team.

It provides visitors with an overview of the people who help manage the server and support its activities.

---

## Automatic YouTube Updates

One of the main technical features of the project is its automated YouTube video-update system.

The website uses a GitHub Actions workflow to retrieve public video metadata from the [Stellar Science Club YouTube channel](https://www.youtube.com/@StellarScienceClub) and update the JSON file consumed by the YouTube page.

### How It Works

The workflow is configured to run every 30 minutes and can also be triggered manually.

The update process follows these steps:

1. **Retrieve video information:** A Python script uses `yt-dlp` to read the public YouTube channel feed.
2. **Collect metadata:** The script retrieves available information, including video IDs, titles, thumbnails, publication information and durations.
3. **Generate JSON:** The collected data is written to `data/videos.json`.
4. **Commit changes:** When the data changes, the workflow commits the updated file to the repository.
5. **Update the website:** GitHub Pages serves the updated website, and the YouTube page reads the refreshed video data.

This separates the video-data collection process from the frontend, so new uploads can appear without requiring the HTML page to be manually edited each time.

### Why Use JSON?

The file `data/videos.json` acts as a structured data source for the YouTube page.

Instead of writing every video directly into the HTML, the page can read the JSON file and generate the video listing dynamically.

This makes the website easier to maintain because video metadata and page layout are handled separately.

### Reliability and Error Handling

The updater is designed to preserve existing video data if a refresh fails or YouTube temporarily blocks a request, rather than replacing the feed with an empty list.

The repository may also contain an initial seeded video entry so that the YouTube page can display content before the first successful automated refresh.

The `updated` field in the JSON file can be used to record when the data was last refreshed, depending on the updater's implementation.

### Running the Workflow Manually

To trigger an update:

1. Open the GitHub repository.
2. Navigate to the **Actions** tab.
3. Select **Update YouTube videos**.
4. Click **Run workflow**.
5. Inspect the workflow logs to check whether the update completed successfully.

The updater uses `yt-dlp` within GitHub Actions to access the public channel feed. It does not require a YouTube API key to be embedded in the website.

---

## Technology Stack

| Technology     | Purpose                                                                  |
| -------------- | ------------------------------------------------------------------------ |
| HTML           | Defines the structure and content of each page.                          |                                                                         |
| JavaScript     | Adds interactive behaviour and loads dynamic video data.                 |
| Python         | Retrieves YouTube metadata and generates the JSON data file.             |
| JSON           | Stores the video information consumed by the frontend.                   |
| GitHub Actions | Automates periodic and manual YouTube data updates.                      |
| GitHub Pages   | Hosts and serves the static website.                                     |
| `yt-dlp`       | Retrieves publicly available YouTube channel and video metadata.         |
| Git and GitHub | Provide version control, source-code hosting and deployment integration. |

## Project Structure

The repository is organised into page files, supporting assets, data and automation scripts.

```text
stellar-science-club-website/
├── index.html
├── features.html
├── study-events.html
├── community.html
├── jmss.html
├── youtube.html
├── team.html
├── data/
│   └── videos.json
├── scripts/
│   └── update_videos.py
├── .github/
│   └── workflows/
│       └── update-youtube.yml
├── assets/
│   ├── stellar-qr.png
```

### Key Files

- **`index.html`** — the homepage.
- **`features.html`** — the community features page.
- **`study-events.html`** — information about study sessions and events.
- **`community.html`** — the Discord channel directory.
- **`jmss.html`** — JMSS preparation information.
- **`youtube.html`** — the YouTube video listing.
- **`team.html`** — information about the club's team.
- **`data/videos.json`** — the video metadata consumed by the front end.
- **`scripts/update_videos.py`** — the Python updater for YouTube metadata.
- **`.github/workflows/update-youtube.yml`** — the scheduled and manually triggered GitHub Actions workflow.

## Hosting and Deployment

The website is hosted using GitHub Pages and is designed to operate as a static website.

The frontend does not require a continuously running server or a database. Its HTML, CSS, JavaScript and JSON files are served as static assets.

The GitHub Actions workflow handles the automated YouTube-data refresh separately. When the workflow updates and commits `data/videos.json`, GitHub Pages can serve the new data without requiring a separate application backend.

The homepage is `index.html`, and the individual HTML pages are stored in the repository root.

## Design and Maintenance

The website is organised into separate pages so that each major part of the community has its own space. Shared styling and navigation help maintain a consistent experience, while page-specific layouts allow each section to present its information appropriately.

When updating the project:

- Keep internal links consistent with the GitHub Pages project URL.
- Ensure shared CSS and JavaScript paths work across all pages.
- Preserve the expected JSON structure when modifying the YouTube updater.
- Check the GitHub Actions logs if video data stops updating.
- Test navigation and responsive layouts after making frontend changes.

## Future Development

Potential areas for further development include:

- Improving the accessibility and responsiveness of every page.
- Expanding the community and educational-resource directories.
- Improving the reliability and monitoring of the YouTube update workflow.
- Adding more ways to explore the club's videos and study resources.
- Continuing to refine the website as the community grows.

---

**Stellar Science Club** is an ongoing project that combines community building, STEM education and web development to make science learning more accessible and collaborative for students.
