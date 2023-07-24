from django.utils.translation import gettext as _


def get_meta():

    return dict(
            Title=_('Hexlet Task Manager'),
            Project_name=_('Task Manager'),
            Users=_('Users'),
            EnterHeader=_('Log in'),
            Entering=_('Sigh in'),
            LogOut=_('Log Out'),
            YouAreLogIn=_('You are logged in'),
            YouAreLogOut=_('You are logged out'),
            Registration=_('Registration'),
            RegisteredSuccessfully=_('User has been registered successfully!'),
            UpdatingSuccessfully=_('User has been updated successfully!'),
            DeletedSuccessfully=_("User deleted successfully"),
            NoUpdatingRight=_('You do not have rights '
                              'to change another user.'),
            DeleteButton=_('Yes, delete'),
            NotAuthorised=_("You are not authorized! Please sign in."),
            Updating=_('Change user'),
            Greetings=_('Hello from Hexlet!'),
            Courses_name=_('Practical programming courses'),
            About=_('Learn more'),
            Hexlet=_('Hexlet'),
            Id=_('ID'),
            UserName=_('Username'),
            FullName=_('Fullname'),
            DateOfCreate=_('Date of creation'),
            FirstName=_('Firstname'),
            LastName=_('Lastname'),
            RequirmentField=_('Obligatory field. No more than 150 characters. '
                              'Only letters, numbers and symbols'),
            Password=_('Password'),
            PasswordRequirment=_('Your password must contain '
                                 'at least 3 characters.'),
            PasswordApproval=_('Password confirmation'),
            PasswordApprovalAgain=_('To confirm, please enter '
                                    'your password again.'),
            Register=_('Register'),
            UpdateUser=_('Change'),
            DeleteUser=_('Delete'),
            DeletingUser=_('Deleting a user'),
            DeletingApproving=_('Are you sure you want to delete'),
            Statuses=_('Statuses'),
            Labels=_('Labels'),
            Tasks=_('Tasks'),
        )
