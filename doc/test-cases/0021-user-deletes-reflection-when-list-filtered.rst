==============================================================
User deletes a reflection when the refleciton list is filtered
==============================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0021
      - 
        * https://github.com/colinfwren/garner/issues/20

====
Setup
====

- There's an existing question in the system
- There's 4 reflections in the system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - 
        * Ensure that there are 4 Reflections in the system
        * 1st Reflection
            * has the word "filter" in the answer text
            * does not have the term "search" in the answer text
            * has the word "both" in the answer text
            * does not have the word "neither" in the answer text]
            * does not have the word "last" in the answer text
        * 2nd Reflection
          * has the word "search" in the answer text
          * does not have the word "filter" in the answer text
          * has the word "both" in the answer text
          * does not have the word "neither" in the answer text
          * does not have the word "last" in the answer text
        * 3rd Reflection
          * does not have the words "search", "filter", "both" or "neither" in the answer text
          * has the term "last" in the answer text
        * 4th Reflection
          * Does not have the words "search", 'filter", "both", "neither" or "last" in the answer text
      -
      - The Reflection list has those four Reflections
    * - Filter the Reflection List using the term "both'
      - 
      - 
        * The first Reflection that was added is shown
        * The second Reflection is shown
        * The third Reflection is not shown
        * The fourth Reflection is not shown
    * - Perform the system specific way of deleting a list item (swipe on iOS to show delete button) to delete the first Reflection
      - 
      - 
        * The Reflection List remains filtered
        * The first Reflection is removed from the filtered list
        * The second Reflection remains in the filtered list
    * - Clear the filter
      - 
      - 
        * The Reflection List does not contain the first Reflection
        * The Reflection List contains the second, third and fourth Reflections
        * The Reflection list can still be filtered as there are two or more reflections
    * - Filter the Reflection List using the term "both"
      - 
      - 
        * The now deleted first Reflection is not shown
        * The second Reflection is shown
        * The third and fourth Reflections is not shown
    * - Perform the system specific way of deleting a list item (swipe on iOS to show delete button) to delete the second Reflection
      - 
      - 
        * The Reflection List remains filtered
        * The second Reflection is no longer shown
        * The user sees a "no results" view
    * - Clear the filter
      - 
      -
        * The Reflection List does not contain the first Reflection
        * The Reflection List does not contain the second Reflection
        * The Reflection List contains the third and fourth Reflections
        * The Reflection list can still be filtered as there are two reflections
    * - Filter the Reflection List using the term "last"
      - 
      - 
        * The now deleted first and second Reflections is not shown
        * The third Reflection is shown
        * The fourth Reflection is not shown
    * - Perform the system specific way of deleting a list item (swipe on iOS to show delete button) to delete the third Reflection
      - 
      - 
        * The Reflection List is still filtered
        * The third Reflection is no longer shown
        * The user sees the "no results" view
    * - Clear the filter
      - 
      - 
        * The Reflection List does not contain the first Reflection
        * The Reflection List does not contain the second Reflection
        * The Reflection List does not contain the third Reflection
        * The Reflection List contains fourth Reflection
        * The Reflection list can no longer be filtered (search bar not shown) as there is only one Reflection in the list