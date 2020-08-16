# Tech Workflows

## Curriculum update workflow
1. Curriculum gets updated
  * Pull request to any module-wide repo
2. Build server runs
  * Ensure all model solutions pass tests
  * Ensure slide documentation is valid
  
3. Build server generates curriculum information
  * Lives in course-wide repo

4. Aiza monitores changes
  * Aiza detects changes on **program-wide** repo and figures out which course to do `get_curriculum` on
  * Aiza detects changes on course-wide repo and initates a get_curriculum call
  
## Cohort start workflow
1. Admin initaties `create_course`
  * Add students and instructors to the course
  
