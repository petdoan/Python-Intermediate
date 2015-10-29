class SuppressErrors:
    def __init__(self, *exceptions):
        """Populate list of exceptions to suppress.
  
        If list is empty, suppress ALL exceptions because all exceptions
        inherit from the base class Exception.
        """

        if not exceptions:
            exceptions = (Exception,)
        self.exceptions = exceptions

    def __enter__(self):
        """Nothing to do here. Exception handling occurs in __exit__()."""
        pass

    def __exit__(self, exc_class, exc_instance, traceback):
        """This method "suppresses" exceptions.

        Exception suppression is performed by virtue of the return value.
        If it completes without a return value, the original exception
        will be re-raised. Returning True catches the exception and
        suppresses it.
        """
         
        if isinstance(exc_instance, self.exceptions):
            return True
        return False
