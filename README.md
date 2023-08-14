# django-rest-api

## Model
Defined two Django models: `Company` and `Employee`. These models represent the structure of your database tables.

1. Company Model:
   >  This model represents a `company` with various fields:

      * `company_id`: An AutoField serving as the primary key of the model.
      * `name`: A CharField with a maximum length of 50 characters to store the company's name.
      * `location`: A CharField with a maximum length of 100 characters to store the company's location.
      * `about`: A TextField to store a more detailed description of the company.
      * `type`: A CharField with predefined choices for the type of company (IT, Non IT, Mobile Phone).
      * `added_date`: A DateTimeField that automatically stores the date and time when the company is added.
      * `active`: A BooleanField with a default value of True, indicating whether the company is active.
      * The `__str__` method returns a string representation of the company using its name and location.

2. Employee Model:
    > This model represents an employee with various fields:

    * `name`: A CharField with a maximum length of 50 characters to store the employee's name.
    * `email`: An EmailField with a maximum length of 50 characters to store the employee's email.
    * `address`: A CharField with a maximum length of 200 characters to store the employee's address.
    * `phone`: A CharField with a maximum length of 10 characters to store the employee's phone number.
    * `about`: A TextField to store a more detailed description of the employee.
    * `position`: A CharField with predefined choices for the employee's position (Manager, Software Developer, Project Leader).
    * `company`: A ForeignKey relationship to the Company model, indicating which company the employee belongs to.
    * The `__str__` method returns a string representation of the employee using their name.
