from django.shortcuts import render

"""
DO NOT USE!!! Instead, create one file per view. The view will have a class 
with all the callable methods. For HTML the methods names are get, post,
push and delete for the basic operations. Example

class FoodPantryAppHomeView(View) -->  food_pantry_app_home_view.py

Something similar will be done for the api views, but using the APIView abstract class

class FoodPantryApiCustomerView(APIView) --> food_pantry_api_customer_view.py
"""