# Property Manager

A data-centric project that provides users the ability to view/manage properties for auction.

## UX

The UX/UI of this website was designed to simple and clear for any end user. Materialize was utilised to achieve this goal where their navigation templates were used.

## Features

View Properties (Homepage)
- A collection of properties that have been added. Expandable div's that contain additional property information.
Add property
- Contains a form that sends user entered property values to the database in order to be viewed later.
Edit Property
- Retrieves fields from the database based on user selection, enabling the user to manipulate the values in related fields.
Delete Property
- Removes the selected property from the database.
Mobile friendly
- Utilizes a side navigation bar to enable mobile usability.

### Future Improvements

- Instead of displaying one photo, show the user a gallery
- Add authentication, allow admins to manage properties while regular users can browse/submit offers.

## Technologies Used

- [GitHub](https://github.com/)
    - The project uses **GitHub** as a code repository
- [Materialize](https://materializecss.com/)
    - The project uses **Materialize** to access pre-constructed styling elements
- [FontAwesome](https://fontawesome.com/)
    - The project uses **FontAwesome** for graphical icons
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to initiate functionality provided my Materialize
- [Heroku](https://heroku.com)
    - The project uses **Heroku** to host the code stored in GitHub
- In addition to the required languages of HTML, CSS & Python(+PyMongo)

## Testing

All forms and buttons work as expected.

Pages usable on mobile/desktop

## Deployment

This project uses Heroku for hosting. Each commit forces a deploy to the platform.

Config vars are utilized in Heroku for the DB relationship.
