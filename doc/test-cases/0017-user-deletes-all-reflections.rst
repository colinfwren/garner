============================
User deletes all reflections
============================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0017
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
        * Reflections to be deleted in in the Reflection List
        * The user does not see the "Add first Reflection" prompt in the Reflection List
    * - Filter Reflection List using text found in one of the Reflection to be deleted
      - 
      - Reflection is included in the filter results
    * - 
        * Ensure the Reflection List is not filtered
        * Perform the platform specific action to delete all Reflections (iOS is Swipe and press delete button)
      - 
      - 
        * Reflections are removed from the Reflection List
        * The user sees the "Add First Reflection" prompt in the Reflection List
    * - Filter the Reflection List using the term that was present in the Reflection that was used to filter the Reflection List earlier
      - 
      - 
        * The Reflection that was deleted is no longer shown in the results
        * The user sees the "No Results" view
    * - View the Settings screen
      - 
      - 
        * "Add First Reflection" prompt is shown
        * User is unable to export data as there is no data to export