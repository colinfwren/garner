===================================================
User updates question list after adding action item
===================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0034
      - 
        * https://github.com/colinfwren/garner/issues/28
        * https://github.com/colinfwren/garner/issues/29

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * -
        * Add 3 Questions to the Question List
        * Press "New Reflection" button
      - 
      - 
        * Should see all 3 Questions in Reflection form
        * Each Question has it’s own Action List
    * - 
        * Add 2 Actions for each Question in the Reflection form
        * Save the new Reflection
      -
      -
        * The new Reflection is added
        * The Actions List on the Growth tab is now populated with 6 Actions in one group based on the creation date
    * - View the Reflection
      - 
      - Each Question has 2 actions against it
    * - 
        * Change the order of the Questions in the Question List
        * View the newly created Reflection
      - 
      - The Reflection should list the same set of Actions against the Questions and the order of the Questions should remain unchanged
    * - Press "New Reflection" button
      - 
      -
        * The Questions should have changed order
        * The Questions still have the Actions that were linked to them shown as being linked to them
    * -
        * Cancel the New Reflection
        * View the Actions List on the Growth Tab
      - 
      - The action list should remain as it was
    * - 
        * Add a new Question to the Question List
        * Press "New Reflection" button
      - 
      - 
        * The Questions still have the Actions that were linked to them shown as being linked to them
        * The new Question has no Actions
    * - 
        * Cancel the New Reflection
        * View the Actions List on the Growth Tab
      -
      - The Actions list should remain unchanged
    * - 
        * Remove one of the Questions that had Actions attached to it from the Question List
        * Press the "New Reflection" button
      -
      - The Questions that haven’t been deleted still have the Actions that were linked to them shown as being linked to them
    * - 
        * Cancel the New Reflection
        * View the Growth tab
      - 
      - 
        * The Actions List should still list the Actions against the Questions that haven’t been deleted
        * The Actions List should still list the Actions against the deleted Question