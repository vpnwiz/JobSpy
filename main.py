import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    # site_name=["indeed", "linkedin", "glassdoor", "zip_recruiter", "google"],
    site_name="linkedin",
    search_term="solutions engineer",
    # google_search_term="software engineer jobs near San Francisco, CA since yesterday",
    location="Cleveland, OH",
    distance=250,
    is_remote=True,
    results_wanted=10,
    hours_old=48,
    country_indeed='USA',
    linkedin_fetch_description=True, # gets more info such as description, direct job url (slower)
    offset=5,
    verbose=2
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel