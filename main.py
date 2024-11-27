import arxiv
import os
import requests

def download_arxiv_papers(query, start_year, end_year, max_results=300, save_path=r"C:\Users\krist\Desktop\Faks\Magisterij 2. letnik\Magistrski raziskovalni seminar\projektnaNaloga\arxiv_papers"):
    os.makedirs(save_path, exist_ok=True)

    print(f"Fetching papers published between {start_year} and {end_year}...")
    
    # Perform the search
    search = arxiv.Search(
        query=query,
        max_results=max_results * 10,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    results_found = 0
    papers_downloaded = 0

    for result in search.results():
        if start_year <= result.published.year <= end_year:
            results_found += 1

            print(f"Title: {result.title}")
            print(f"Authors: {', '.join([author.name for author in result.authors])}")
            print(f"Published: {result.published}")
            print(f"URL: {result.entry_id}")
            print("-" * 50)

            sanitized_title = result.title.replace(" ", "_").replace("/", "_").replace(":", "_")
            filename = f"{result.published.year}_{sanitized_title}.pdf"
            filepath = os.path.join(save_path, filename)

            print(f"Downloading: {result.title}")
            try:
                response = requests.get(result.pdf_url, stream=True)
                if response.status_code == 200:
                    with open(filepath, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=1024):
                            f.write(chunk)
                    print(f"Downloaded to {filepath}\n")
                    papers_downloaded += 1
                else:
                    print(f"Failed to download: {result.title} (HTTP {response.status_code})")
            except Exception as e:
                print(f"Error downloading {result.title}: {e}")

            if papers_downloaded >= max_results:
                break

    print(f"Total papers found in range {start_year}–{end_year}: {results_found}")
    print(f"Total papers downloaded: {papers_downloaded}")

if __name__ == "__main__":
    download_arxiv_papers(
        query="pancreatic cancer",
        start_year=2022,
        end_year=2024,
        max_results=300,
        save_path=r"C:\Users\krist\Desktop\Faks\Magisterij 2. letnik\Magistrski raziskovalni seminar\projektnaNaloga\arxiv_papers"
    )
