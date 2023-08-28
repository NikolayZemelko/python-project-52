from django.utils.translation import gettext as _


def get_meta():
    return dict(
        Main=dict(
            Author=_('Author'),
            Executor=_('Executor'),
            Title=_('Hexlet Task Manager'),
            Project_name=_('Task Manager'),
            Users=_('Users'),
            Statuses=_('Statuses'),
            Labels=_('Labels'),
            Tasks=_('Tasks'),
            EnterHeader=_('Log in'),
            Entering=_('Sigh in'),
            LogOut=_('Logout'),
            Show=_('Show'),
            Registration=_('Registration'),
            Description=_('Description'),
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
            DeletingApproving=_('Are you sure you want to delete'),
            Update=_('Change'),
            Delete=_('Delete'),
            Empty=_('---------')
        ),
        Users=dict(
            UserName=_('Username'),
            FullName=_('Fullname'),
            FirstName=_('Firstname'),
            LastName=_('Lastname'),
            Updating=_('Change user'),
            Executor=_('Executor'),
            RegisteredSuccess=_('User has been '
                                'registered successfully!'),
            UpdatingSuccess=_('User has been updated successfully!'),
            DeletedSuccess=_("User deleted successfully"),
            DeletingUser=_('Deleting a user'),
            Password=_('Password'),
            PasswordRequirment=_('Your password must contain '
                                 'at least 3 characters.'),
            PasswordApproval=_('Password confirmation'),
            PasswordApprovalAgain=_('To confirm, please enter '
                                    'your password again.'),
            PasswordConfReq=_('Enter the same password as before, '
                              'for verification.'),
            Pass1HelpText=_('Your password must contain '
                            'at least 3 characters.'),
            UserNameReq=_('Required. 150 characters or fewer. '
                          'Letters, digits and @/./+/-/_ only.'),
            NotAuthorised=_("You are not authorized! Please sign in."),
            YouAreLogIn=_('You are logged in'),
            YouAreLogOut=_('You are logged out'),
            UserInWork=_('Cannot delete user because it is in use')
        ),
        Statuses=dict(
            Status=_('Status'),
            CreateStatus=_('Create status'),
            UpdateStatus=_('Change status'),
            DeleteStatus=_('Delete status'),
            CreatedSuccess=_('Status created successfully'),
            UpdatedSuccess=_('Status has been updated successfully!'),
            DeletedSuccess=_("Status deleted successfully"),
            StatusInWork=_("Can't delete status because it's in use")
        ),
        Tasks=dict(
            CreateTask=_('Create task'),
            UpdateTask=_('Update task'),
            DeleteTask=_('Delete task'),
            ViewTask=_('View task'),
            CreatedSuccess=_('Task created successfully'),
            UpdatedSuccess=_('Task changed successfully'),
            DeletedSuccess=_('Task deleted successfully'),
            OnlyAuthorCanDel=_('A task can only be '
                               'deleted by its author.'),
            OnlyYourTasks=_('Only your tasks'),

        ),
        Labels=dict(
            Label=_('Label'),
            CreateLabel=_('Create label'),
            UpdateLabel=_('Update label'),
            DeleteLabel=_('Delete label'),
            CreatedSuccess=_('Label created successfully'),
            UpdatedSuccess=_('Label changed successfully'),
            DeletedSuccess=_('Label deleted successfully'),
            LabelInWork=_("Can't delete label because it's in use")
        ),
    )
