=========================
User exports a reflection
=========================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0029
      - 
        * https://github.com/colinfwren/garner/issues/24
        * https://github.com/colinfwren/garner/issues/18

====
Setup
====

- There's at least 1 question in the system
- There's at least 1 reflection in the system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - View the Reflection List
      - 
      - 
        * Note the Reflection order
        * Note the creation dates of the Reflections
        * Note the Questions for the Reflections
        * Note the Answers for the Reflections
    * - Export data
      - 
      - 
        * The UI updates to inform the user that the export is being generated
          * The Export Data button cannot be pressed
        * Once the export has been generated the user is presented with the system’s share UI so the user can save the file or share it via another service
    * - Save file to file system
      - 
      - 
        * The file is saved to the file system with a `.md`` extension
        * The file is saved to the file system with the name `garner-export-[year of export]-[month of export]-[date-of-export]`
        * Reflections in the file are listed in the export in reverse chronological order
        * Each Reflection has a heading with the create date of the Reflection
        * Under each Reflection’s heading are sub-headings for the Questions in the Reflection Configuration used for that Reflection
        * Under each Question sub-heading is the text for the answer
  