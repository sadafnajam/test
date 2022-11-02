# Conda App

This app demonstrates how deploy an app that uses `conda` and `environment.yml`

## Run the App Locally

1. Install the required Python packages using conda:
   ```
   conda env create -f environment.yml 
   ```
2. Verify the packages installed via conda
   ```
   conda list
   ```
3. Activate conda virtual environment
   ```
   conda activate test-env
   ```
4. Run the app
   ```
   gunicorn app:server --workers 1
   ```


## Deploy the App to Dash Enterprise

To deploy this app to Dash Enterprise, [initialize an app]({base_url}/dash-enterprise/initialize), and then follow [the steps for deployment]({base_url}/dash-enterprise/deployment).