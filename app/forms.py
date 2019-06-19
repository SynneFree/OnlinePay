from wtforms.fields import simple, core
from wtforms import Form, validators, widgets, ValidationError
from .models import verify_user_register
import calendar


class LoginForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    password = simple.PasswordField(
        label='Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput()
    )


class RechargeForm(Form):
    cardnumber = simple.StringField(
        label='Card number',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    password = simple.PasswordField(
        label='Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput()
    )


class RegistrationForm(Form):
    def validate_realname(self, field):
        if verify_user_register(self.realname.data,self.citizenid.data):
            pass
        raise ValidationError(u'Real Name not match CitizenId')

    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    password = simple.PasswordField(
        label='Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    password2 = simple.PasswordField(
        label='Repeat Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty'),
                    validators.EqualTo('password',message='Two password not same')])
    paypassword = simple.PasswordField(
        label='PayPassword',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    paypassword2 = simple.PasswordField(
        label='Repeat PayPassword',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty'),
                    validators.EqualTo('paypassword',message='Two password not same')])
    realname = simple.StringField(
        label='Real name',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="RealName can not be empty")])
    citizenid = simple.StringField(
        label='Citizen ID',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Citizen ID can not be empty"),validate_realname])
    email = simple.StringField(
        label='Email',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message='Email can not be empty'),
                    validators.Email(message='Wrong Email Syntax')])
    phone = simple.StringField(
        label='Phone',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="phone can not be empty")])
    typeid = simple.BooleanField(
        label='IS Buyer',
        widget=widgets.CheckboxInput())
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())


class AddManagerForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    password = simple.PasswordField(
        label='Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    AuthenticationPassword = simple.PasswordField(
        label='AuthenticationPassword',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    checker = simple.BooleanField(
        label='Create checker',
        widget=widgets.CheckboxInput())
    admin = simple.BooleanField(
        label='Create admin',
        widget=widgets.CheckboxInput())
    Super_admin = simple.BooleanField(
        label='Create super admin',
        widget=widgets.CheckboxInput())
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())


class DeleteManagerForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])


class MaintainUserForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput())
    type = core.SelectField(
        label="UserType",
        choices=[
            (1, "Seller"),
            (2, "Buyer-Ordinary"),
            (3, "Buyer-VIP"),
        ],
        coerce=int
    )
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())


class MaintainManagerForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    deleteright = simple.BooleanField(
        label='DeleteRight',
        widget=widgets.CheckboxInput())
    addright = simple.BooleanField(
        label='AddRight',
        widget=widgets.CheckboxInput())
    arbitrationright = simple.BooleanField(
        label='ArbitrationRight',
        widget=widgets.CheckboxInput())
    blacklistright = simple.BooleanField(
        label='BlackListRight',
        widget=widgets.CheckboxInput())
    viewright = simple.BooleanField(
        label='ViewRight',
        widget=widgets.CheckboxInput())


class BillForm(Form):
    MONTHS = [(str(0), 'ALL')]
    for i in range(1, 13):
        MONTHS.append((str(i), calendar.month_name[i]))
    year = core.IntegerField(
        label='Year',
        validators=[validators.NumberRange(min=1970, max=2019)])
    month = core.SelectField(choices=MONTHS)
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())


class loginpswdmodifyform(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput())
    password = simple.PasswordField(
        label='Old Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    password2 = simple.PasswordField(
        label='Repeat Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty'),
                    validators.EqualTo('password', message='Two password not same')])
    newpassword = simple.PasswordField(
        label='New Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    email = simple.StringField(
        label='Email',
        widget=widgets.TextInput())
    phone = simple.StringField(
        label='Phone',
        widget=widgets.TextInput())
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())

class paypswdmodifyform(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput())
    password = simple.PasswordField(
        label='Old PayPassword',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    password2 = simple.PasswordField(
        label='Repeat the Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty'),
                    validators.EqualTo('password', message='Two password not same')])
    newpassword = simple.PasswordField(
        label='New PayPassword',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    email = simple.StringField(
        label='Email',
        widget=widgets.TextInput())
    phone = simple.StringField(
        label='Phone',
        widget=widgets.TextInput())
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())



class ModifyForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput())
    email = simple.StringField(
        label='Email',
        widget=widgets.TextInput())
    phone = simple.StringField(
        label='Phone',
        widget=widgets.TextInput())
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())


class AddBlacklistsForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    typeid = simple.BooleanField(
        label='IS Buyer',
        widget=widgets.CheckboxInput())
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())

class DeleteBlacklistsForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    typeid = simple.BooleanField(
        label='IS Buyer',
        widget=widgets.CheckboxInput())
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())

class AddGoodForm(Form):
    goodname = simple.StringField(
        label= 'Goodname',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Goodname can not be empty")])
    price = simple.FloatField(
        lable = 'Price',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Price can not be empty")])
    sellerid = simple.StringField(
        label='Sellerid',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Sellerid can not be empty")])
    From = simple.StringField(
        label = 'From',
        widget=widgets.TextInput())
    dest = simple.StringField(
        label = 'Dest',
        widget=widgets.TextInput())


# **********************************************************
# *********************** Group 3 **************************
# **********************************************************



class QueryGoodsForm(Form):
    goodname = simple.StringField(
        label='查询商品',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Goodname can not be empty")])