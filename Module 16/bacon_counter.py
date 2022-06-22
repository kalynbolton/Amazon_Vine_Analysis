from mrjob.job import MRJob
# create class 
class Bacon_count(MRJob):
# create function that will take parameters that will asign input to key-value pairs
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1 

# add reducer function
    def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()