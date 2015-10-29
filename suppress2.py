import traceback

class SuppressErrors:
    def __init__(self, *exceptions):
        """Populate list of exceptions to suppress.
  
        If list is empty, suppress ALL exceptions because all exceptions
        inherit from the base class Exception.
        """

        print("in __init__() method of SuppressErrors")
     
        if not exceptions:
            print("ALL exceptions will be suppressed.")
            exceptions = (Exception,)
        else:
            print("Only these exceptions will be suppressed: ", end="")
            for exc in exceptions:
                print("{} ".format(exc.__name__), end="")
            print()

        self.exceptions = exceptions

    def __enter__(self):
        """Nothing to do here.
    
        Exception handling occurs in __exit__().
        NOTE: Whatever is returned from this method will be 
        used to populate the variable in the 'as' clause'''
        """
        print("in __enter__() method of SuppressErrors")
        return 'test'

    def __exit__(self, exc_class, exc_instance, tb):
        """This method "suppresses" exceptions.
        Exception suppression is performed by virtue of the return value.
        If it completes without a return value, the original exception
        will be re-raised. Returning True catches the exception and
        suppresses it.
        """
         
        print("in __exit__() method of SuppressErrors")
        traceback.print_tb(tb)
        if isinstance(exc_instance, self.exceptions):
            return True
        # What happens if we don't return anything?

