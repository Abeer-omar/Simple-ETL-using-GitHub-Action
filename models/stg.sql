{{ config(materialized='view') }}

select
    employee_id,
    first_name,
    department,
    salary,
    tax,
    net_salary,
    employment_type
from public.transformed_employees