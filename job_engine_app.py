import streamlit as st
from serpapi.google_search import GoogleSearch

class JobSearchEngine:
    def __init__(self):
        """
        Initializes the JobSearchEngine instance by loading environment variables.
        This setup is essential for the search engine to access API keys for job search requests.
        """
        self.load_env_variables()

    def load_env_variables(self):
        """
        Loads environmental variables from a .env file, specifically the SERPAPI_API_KEY
        used for job search requests. This API key is essential for making requests to the search API.
        """
        self.api_key = st.secrets["api_key"]

    def select_job_criteria(self):
        """
        Provides an interface for the user to input job search criteria such as job title
        and location. This input is made through a graphical interface, leveraging text input boxes.
        """
        self.job_title = st.text_input("Job Title", value="Software Developer")
        self.location = st.text_input("Location", value="New York")

    def search_jobs(self):
        """
        Triggers the job search based on input criteria upon user request.
        Utilizes the SERPAPI for fetching job options and then processes these options
        to display them to the user.
        """
        if st.button("Search Jobs"):
            params = {
                "engine": "google_jobs",
                "q": self.job_title,
                "ltype": "1",
                "hl": "en",
                "api_key": self.api_key
            }
            search = GoogleSearch(params)
            results = search.get_dict()
            self.display_results(results.get("jobs_results", []))

    def display_results(self, jobs_results):
        if jobs_results:
            for job in jobs_results:
                job_title = job.get("title", "N/A")
                company_name = job.get("company_name", "N/A")
                location = job.get("location", "N/A")
                description = job.get("description", "N/A")
                expander_title = f"{job_title} at {company_name} ({location})"
                job_expander = st.expander(expander_title, expanded=False)
                
                with job_expander:
                    # Display the job thumbnail if available
                    if job.get("thumbnail"):
                        st.image(job["thumbnail"], width=70)
                    
                    st.markdown(f"**Description:** {description}")
                    
                    # Handle job highlights
                    job_highlights = job.get("job_highlights", [])
                    for highlight in job_highlights:
                        highlight_title = highlight.get("title", "Detail")
                        st.markdown(f"**{highlight_title}:**")
                        for item in highlight.get("items", []):
                            st.write(f"- {item}")
                    
                    # Show extensions such as posting time, work from home availability, etc.
                    if "extensions" in job:
                        for extension in job["extensions"]:
                            st.write(extension)
        else:
            st.write("No jobs found.")


def main():
    st.title('Job Search Engine')
    engine = JobSearchEngine()
    engine.select_job_criteria()
    engine.search_jobs()

if __name__ == "__main__":
    main()
