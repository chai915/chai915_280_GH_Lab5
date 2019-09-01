import unittest     # Import the Python unit testing framework
import logger
import log_target


class LoggerTest(unittest.TestCase):
    ''' Unit tests for our logger functions. '''
    
    def test_info(self):
        info_target = log_target.LogTarget()
        
        loggerInfo = logger.Logger(info_target.set_message)
        loggerInfo.info("I am a log message")
        
        
        
        self.assertEqual(info_target.get_message(), "[INFO] I am a log message")
        
    
    def test_error(self):
        error_target = log_target.LogTarget()
        
        loggerError = logger.Logger(error_target.set_message)
        loggerError.error("ALERT ERROR")
        
        self.assertEqual(error_target.get_message(), "[WARNING] ALERT ERROR")
    
if __name__ == '__main__':
    unittest.main()