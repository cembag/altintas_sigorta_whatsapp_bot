from datetime import datetime, timedelta


class DateService: 

    def getDiffFirebaseDateFromNowByHours(self, firebaseTimestamp) -> timedelta:
        firebaseDate = self.firebaseDateToDatetime(firebaseTimestamp)
        dateNow = datetime.now()
        difference = firebaseDate - dateNow
        return difference.total_seconds() / 3600
    
    def getDiffFromDatetimes(self, date1: datetime, date2: datetime) -> timedelta: 
        return date1 - date2

    def firebaseDateToDatetime(self, date) -> datetime:
        return datetime.fromtimestamp(date.timestamp()).utcnow()