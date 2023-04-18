# egentligen vasilis kod från canvas menmen

import pandas as pd 

jobtech_dataset = pd.read_json('2022.sample.json')
print(jobtech_dataset.columns)
print(jobtech_dataset.head(3))

### samtliga kolumner i datasetet: ###
#['id', 'external_id', 'webpage_url', 'logo_url', 'headline','application_deadline', 'number_of_vacancies', 'description',
# 'employment_type', 'salary_type', 'salary_description', 'duration',
# 'working_hours_type', 'scope_of_work', 'access', 'employer',
# 'application_details', 'experience_required', 'access_to_own_car',
# 'driving_license_required', 'driving_license', 'occupation',
# 'occupation_group', 'occupation_field', 'workplace_address',
# 'must_have', 'nice_to_have', 'application_contacts', 'publication_date',
# 'last_publication_date', 'removed', 'removed_date', 'source_type','timestamp'], dtype='object')

# intressant för oss är väl experience_required, must_have, nice_to_have, kanske descprition?, employment_type


