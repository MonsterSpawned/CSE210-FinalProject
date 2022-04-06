from datetime import datetime
import pytz
class DateTimeUtils():
    
    # Initialize the datetime object, etc.
    def __init__(self, tz: str = 'America/Denver'):
        local_tz = pytz.timezone(tz)
        self.dt_now = datetime.now(local_tz)
        self.local_datetime = local_tz.localize(datetime.now())
        
    # Get the current system date.
    def get_current_date(self, format: str = '%B %d, %Y'):
        """
        Gets the current date as a string.
        """
        return self.local_datetime.strftime(format)
    
    # Get the current time.
    def get_current_time(self):
        """
        Gets the current time as a string.
        """
        hours =     f"{self.dt_now.hour}"
        minutes =   f"{self.dt_now.minute}"
        seconds =   f"{self.dt_now.second}"
        
        if self.dt_now.hour > 12:
            hours = f"{self.dt_now.hour-12}"
        if self.dt_now.second < 10:
            seconds = f"0{self.dt_now.second}"
        if self.dt_now.minute < 10:
            minutes = f"0{self.dt_now.minute}"
        return f"{hours}:{minutes}:{seconds}"
    
    
        
    
    