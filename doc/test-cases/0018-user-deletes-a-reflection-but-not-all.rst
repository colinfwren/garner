=====================================
User deletes a reflection but not all
=====================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0018
      - 
        * https://github.com/colinfwren/garner/issues/16

====
Setup
====

- There's an existing question in the system
- There's at least 3 existing reflections in the system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - View reflection list
      - 
      - there's at least 3 reflections in the list
    * - Export Data
      - 
      - Reflections to be deleted is included in the exported data
    * - View Reflection List
      - 
      - 
        * There are at least 3 Reflections in the Reflections List
        * The Reflection List can be filtered
        * Reflection to be deleted in in the Reflection List
        * The user does not see the "Add first Reflection" prompt in the Reflection List
    * - Filter Reflection List using text found in two of the Reflections, including the Reflection to be deleted
      - 
      - Reflection is included in the filter results
    * - 
        * Ensure the Reflection List is not filtered
        * Perform the platform specific action to delete 1 Reflection (iOS is Swipe and press delete button)
      - 
      - 
        * Reflection is removed from the Reflection List
        * User does not see the "Add First Reflection" prompt as there are Reflections in the Reflection List
    * - Filter the Reflection List using the term that was present in the Reflection that was used to filter the Reflection List earlier
      - 
      - 
        * The Reflection that was deleted is no longer shown in the results
        * The other Reflections that match the search term are shown
    * - Export data from app
      - 
      - The Reflection that was deleted is no longer present in the export