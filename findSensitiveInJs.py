import re
import requests
import sys
import threading
import colorama
from colorama import Fore, Style

def extract_sensitive_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        pattern = re.compile(r'(?i)\b(access_key|access_token|admin_pass|admin_user|algolia_admin_key|algolia_api_key|alias_pass|alicloud_access_key|amazon_secret_access_key|amazonaws|ansible_vault_password|aos_key|api_key|api_key_secret|api_key_sid|api_secret|api.googlemaps AIza|apidocs|apikey|apiSecret|app_debug|app_id|app_key|app_log_level|app_secret|appkey|appkeysecret|application_key|appsecret|appspot|auth_token|authorizationToken|authsecret|aws_access|aws_access_key_id|aws_bucket|aws_key|aws_secret|aws_secret_key|aws_token|AWSSecretKey|b2_app_key|bashrc password|bintray_apikey|bintray_gpg_password|bintray_key|bintraykey|bluemix_api_key|bluemix_pass|browserstack_access_key|bucket_password|bucketeer_aws_access_key_id|bucketeer_aws_secret_access_key|built_branch_deploy_key|bx_password|cache_driver|cache_s3_secret_key|cattle_access_key|cattle_secret_key|certificate_password|ci_deploy_password|client_secret|client_zpk_secret_key|clojars_password|cloud_api_key|cloud_watch_aws_access_key|cloudant_password|cloudflare_api_key|cloudflare_auth_key|cloudinary_api_secret|cloudinary_name|codecov_token|config|conn.login|connectionstring|consumer_key|consumer_secret|credentials|cypress_record_key|database_password|database_schema_test|datadog_api_key|datadog_app_key|db_password|db_server|db_username|dbpasswd|dbpassword|dbuser|deploy_password|digitalocean_ssh_key_body|digitalocean_ssh_key_ids|docker_hub_password|docker_key|docker_pass|docker_passwd|docker_password|dockerhub_password|dockerhubpassword|dot-files|dotfiles|droplet_travis_password|dynamoaccesskeyid|dynamosecretaccesskey|elastica_host|elastica_port|elasticsearch_password|encryption_key|encryption_password|env.heroku_api_key|env.sonatype_password|eureka.awssecretkey)\b')
        matches = re.findall(pattern, response.text)
        if matches:
            print(f"Sensitive information found in the response from URL: {url}")
            for match in matches:
                print(Fore.RED + f"- {match}" + Style.RESET_ALL)

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        num_threads = int(sys.argv[2])
    except:
        print("Usage: python script.py <file_name> <num_threads>")
        sys.exit(1)
    
    colorama.init()

    with open(file_name) as f:
        urls = [url.strip() for url in f.readlines()]

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=extract_sensitive_info, args=(urls[i],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
