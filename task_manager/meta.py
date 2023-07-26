from django.utils.translation import gettext as _


def get_meta():

    return dict(
            Main=dict(
                    Title=_('Hexlet Task Manager'),
                    Project_name=_('Task Manager'),
                    Users=_('Users'),
                    Statuses=_('Statuses'),
                    Labels=_('Labels'),
                    Tasks=_('Tasks'),
                    EnterHeader=_('Log in'),
                    Entering=_('Sigh in'),
                    LogOut=_('Log Out'),
                    Registration=_('Registration'),
                    Register=_('Register'),
                    NoUpdatingRight=_('You do not have rights '
                                      'to change another user.'),
                    CreateButton=_('Create'),
                    DeleteButton=_('Yes, delete'),
                    Greetings=_('Hello from Hexlet!'),
                    Courses_name=_('Practical programming courses'),
                    About=_('Learn more'),
                    Hexlet=_('Hexlet'),
                    Id=_('ID'),
                    Name=_('Name'),
                    DateOfCreate=_('Date of creation'),
                    RequirmentField=_('Obligatory field. No more than 150 characters. '
                                      'Only letters, numbers and symbols'),
                    DeletingApproving=_('Are you sure you want to delete'),
                    Update=_('Change'),
                    Delete=_('Delete'),
            ),
            Users=dict(
                    UserName=_('Username'),
                    FullName=_('Fullname'),
                    FirstName=_('Firstname'),
                    LastName=_('Lastname'),
                    Updating=_('Change user'),
                    RegisteredSuccess=_('User has been registered successfully!'),
                    UpdatingSuccess=_('User has been updated successfully!'),
                    DeletedSuccess=_("User deleted successfully"),
                    DeletingUser=_('Deleting a user'),
                    Password=_('Password'),
                    PasswordRequirment=_('Your password must contain '
                                         'at least 3 characters.'),
                    PasswordApproval=_('Password confirmation'),
                    PasswordApprovalAgain=_('To confirm, please enter '
                                            'your password again.'),
                    NotAuthorised=_("You are not authorized! Please sign in."),
                    YouAreLogIn=_('You are logged in'),
                    YouAreLogOut=_('You are logged out'),
                ),
            Statuses=dict(
                    CreateStatus=_('Create status'),
                    UpdateStatus=_('Change status'),
                    DeleteStatus=_('Delete status'),
                    CreatedSuccess=_('Status created successfully'),
                    UpdatedSuccess=_('Status has been updated successfully!'),
                    DeletedSuccess=_("Status deleted successfully"),
            ),
    )
