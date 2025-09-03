================================
User filters the reflection list
================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0020
      - 
        * https://github.com/colinfwren/garner/issues/20

====
Setup
====

- There's an existing question in the system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - 
        * View the Reflection List
        * Delete all Reflections in the Reflection list
      - 
      - 
        * The Reflection List has no Reflections in it
        * The "Add First Reflection" prompt is shown
        * The list does not show the UI to filter the list
    * - 
        * Add a new Reflection
        * Add the term "filter" in an answer,
        * do not add the term "search" anywhere in the answer text
        * Add the term "both" in the answer text
        * do not add the term "neither" anywhere in the answer text
      - 
      - 
        * The Reflection List is updated with the newly added Reflection
        * The Reflection list does not had the "Add First Reflection" prompt
        * The Reflection List does not show the search bar as there’s only one Reflection
    * -
        * Add a new Reflection
        * Add the term "search" in an answer
        * do not add the term "filter" anywhere in the answer text
        * Add the term "both" in the answer text
        * do not add the term "neither" anywhere in the answer text
      -
      - 
        * The Reflection List is updated with the newly added Reflection
        * The Reflection list does not had the "Add First Reflection" prompt
        * The Reflection List does show the search bar as there’s now two Reflections
    * - Filter the Reflection List using the term "filter"
      -
      -
        * The first Reflection that was added is shown
        * The second Reflection that was added is not shown
    * - 
        * Open the Reflection in the filtered list
        * Press back button to go back to Reflection List
      - 
      - 
        * The user is navigated to the Reflection detail for the Reflection
        * On navigating back the Reflection list is still filtered via the term "filter"
    * - Clear the filter
      - 
      - Both Reflections that were added are shown
    * - Filter the Reflection List using the term "search"
      - 
      - 
        * The first Reflection that was added is not shown
        * The second Reflection that was added is shown
    * - 
        * Open the Reflection in the filtered list
        * Press back button to go back to Reflection List
      - 
      - 
        * The user is navigated to the Reflection detail for the Reflection
        * On navigating back the Reflection list is still filtered via the term "search"
    * - Clear the filter
      - 
      - Both Reflections that were added are shown
    * - Filter the Reflection List using the term "both"
      - 
      - 
        * The first Reflection that was added is shown
        * The second Reflection that was is shown
        * The order of the results list is still in reverse chronological order
    * - 
        * Open the Reflection in the filtered list
        * Press back button to go back to Reflection List
      - 
      - 
        * The user is navigated to the Reflection detail for the Reflection
        * On navigating back the Reflection list is still filtered via the term "both"
    * - Clear the filter
      - 
      - Both Reflections that were added are shown
    * - Filter the list using the term "neither'
      - 
      - 
        * The first Reflection that was added is not shown
        * The second Reflection that was added is not shown
        * The user sees a "No Results" view
    * - Clear the filter
      - 
      - Both Reflections that were added are shown