Project Overview
This project was developed for Grazioso Salvare, an organization that identifies and trains search-and-rescue animals. The application utilizes a Python CRUD module to interface with a MongoDB database and a Dash (Plotly) web application to provide a dynamic user interface featuring interactive tables, geolocation maps, and data charts.

Technical Reflection
Maintainability, Readability, and Adaptability
I write maintainable and adaptable programs by adhering to the principle of separation of concerns. By developing a standalone Python CRUD module to handle database interactions, I created a modular system that is easy to troubleshoot and update.

The Advantage: Decoupling the database logic from the dashboard UI allows for easier updates. If the database schema changes or the organization migrates to a different database, I only need to update the CRUD module rather than the entire dashboard application.

Future Use: This CRUD module serves as a robust template for any future Python application requiring secure, authenticated access to a NoSQL database. It can be easily adapted for inventory systems, customer logs, or other data-driven backends.

The Computer Scientist’s Approach
Approaching a problem as a computer scientist means looking past surface requirements to understand the underlying data architecture. For Grazioso Salvare, I focused on how data was indexed and queried to ensure the dashboard remained responsive even when handling large datasets.

Approach to Requirements: I approached the client's requirements by breaking down the "Search and Rescue" criteria into specific database filters. This project differed from previous courses by requiring a full-stack integration of a database, a middleware Python layer, and a frontend visualization tool.

Future Strategies: When meeting client requests in the future, I will continue to prioritize a "requirements-first" design, identifying the specific questions the client needs to answer before building the database schema.

The Role of Computer Science in Business
Computer scientists act as the bridge between raw data and actionable insights. By building this dashboard, I empowered Grazioso Salvare to make data-driven decisions quickly. Instead of manually searching through thousands of records, they can now identify potential rescue candidates in seconds using customized filters. This transforms "noise" into "knowledge," allowing companies to operate more efficiently and—in the case of Grazioso Salvare—ultimately save lives by getting the right animals into training faster.
