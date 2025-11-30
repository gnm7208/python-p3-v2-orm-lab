#!/usr/bin/env python3
"""
Demo script showing Review ORM functionality
"""

from lib.department import Department
from lib.employee import Employee
from lib.review import Review

def main():
    # Create tables
    Department.create_table()
    Employee.create_table()
    Review.create_table()
    
    # Create a department
    dept = Department.create("Engineering", "Building A")
    print(f"Created department: {dept}")
    
    # Create an employee
    emp = Employee.create("Alice Smith", "Software Engineer", dept.id)
    print(f"Created employee: {emp}")
    
    # Create reviews for the employee
    review1 = Review.create(2022, "Excellent Python skills and teamwork", emp.id)
    review2 = Review.create(2023, "Outstanding performance and leadership", emp.id)
    
    print(f"Created review 1: {review1}")
    print(f"Created review 2: {review2}")
    
    # Get all reviews for the employee
    employee_reviews = emp.reviews()
    print(f"\nEmployee {emp.name} has {len(employee_reviews)} reviews:")
    for review in employee_reviews:
        print(f"  - {review.year}: {review.summary}")
    
    # Update a review
    review1.summary = "Exceptional Python skills and excellent teamwork"
    review1.update()
    print(f"\nUpdated review: {review1}")
    
    # Get all reviews
    all_reviews = Review.get_all()
    print(f"\nTotal reviews in database: {len(all_reviews)}")

if __name__ == "__main__":
    main()