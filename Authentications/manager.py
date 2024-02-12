from django.contrib.auth.base_user import BaseUserManager

# In this we customize BaseUserManager and use it for our CustomUser
class CustomerUserManager(BaseUserManager):
    
    # create_user function create user with isActive True and isStaff and isSuperUser as false
    # by default  isStaff and isSuperUser is set to false
    def create_user(self,email, password, **extra_fields):
        # validate email is not none
        if not email:
            # if it is then Raise error
            raise ValueError("The given email must be set")
        # we are using normalize_email so that we can convert 
        # AdityaSahu@Example.com to AdityaSahu@example.com
        email = self.normalize_email(email)
        # creating user 
        user = self.model(email=email, **extra_fields)
        # and using set Password becuase it saves the password in hash
        user.set_password(password)
        # save the user
        user.save(using=self._db)
        # return the user
        return user

    # create_superuser function create user with isActive True and isStaff and isSuperUser as True
    def create_superuser(self,email, password, **extra_fields):
        # as we know the is staff and is super user is set default False 
        # so here we are setting them true for super user
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        # here we are checking if they set true or not 
        if extra_fields.get("is_staff") is not True:
            # if not the raise error
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        # call create user function for super user which return's user
        return self.create_user(email,password,**extra_fields)
