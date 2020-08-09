# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab



class NoChildException(Exception):
	"""
	NoChildException is raised by the reproduce() method in the SimpleVirus
	and ResistantVirus classes to indicate that a virus particle does not
	reproduce. You can use NoChildException as is, you do not need to
	modify/add any code.
	"""    

#
# PROBLEM 1
#

class SimpleVirus():
	"""
	Representation of a simple virus (does not model drug effects/resistance).
	"""
	
	def __init__(self, maxBirthProb, clearProb):
		"""
		Initialize a SimpleVirus instance, saves all parameters as attributes
		of the instance.        
		
		maxBirthProb: Maximum reproduction probability (a float between 0-1)        
		
		clearProb: Maximum clearance probability (a float between 0-1).
		"""
		# TODO
		self.maxBirthProb = maxBirthProb
		self.clearProb = clearProb      

		
	def doesClear(self):
		"""
		Stochastically determines whether this virus is cleared from the
		patient's body at a time step. 

		returns: Using a random number generator (random.random()), this method
		returns True with probability self.clearProb and otherwise returns
		False.
		"""
		# TODO
		if random.random() <= self.clearProb:
			return True
		else:
			return False 


	
	def reproduce(self, popDensity):
		"""
		Stochastically determines whether this virus particle reproduces at a
		time step. Called by the update() method in the SimplePatient and
		Patient classes. The virus particle reproduces with probability
		self.maxBirthProb * (1 - popDensity).
		
		If this virus particle reproduces, then reproduce() creates and returns
		the instance of the offspring SimpleVirus (which has the same
		maxBirthProb and clearProb values as its parent).         

		popDensity: the population density (a float), defined as the current
		virus population divided by the maximum population.         
		
		returns: a new instance of the SimpleVirus class representing the
		offspring of this virus particle. The child should have the same
		maxBirthProb and clearProb values as this virus. Raises a
		NoChildException if this virus particle does not reproduce.               
		"""
		# TODO
		if random.random() <= (self.maxBirthProb*(1 - popDensity)):
			return SimpleVirus(self.maxBirthProb, self.clearProb)
		else:
			raise NoChildException()


class SimplePatient(object):
	"""
	Representation of a simplified patient. The patient does not take any drugs
	and his/her virus populations have no drug resistance.
	"""
	
	def __init__(self, viruses, maxPop):
		"""
		Initialization function, saves the viruses and maxPop parameters as
		attributes.

		viruses: the list representing the virus population (a list of
		SimpleVirus instances)
		
		maxPop: the  maximum virus population for this patient (an integer)
		"""
		# TODO

		self.viruses = viruses
		self.maxPop = maxPop

	def getTotalPop(self):
		"""
		Gets the current total virus population. 

		returns: The total virus population (an integer)
		"""
		# TODO      
		return len(self.viruses)


	def update(self):
		"""
		Update the state of the virus population in this patient for a single
		time step. update() should execute the following steps in this order:

		- Determine whether each virus particle survives and updates the list
		  of virus particles accordingly.

		- The current population density is calculated. This population density
		  value is used until the next call to update() 

		- Determine whether each virus particle should reproduce and add
		  offspring virus particles to the list of viruses in this patient.                    

		returns: the total virus population at the end of the update (an
		integer)
		"""
		# TODO
		newviruses = []
		for i in (self.viruses):
			if  i.doesClear():
				self.viruses.remove(i)
			else: 
				PopDensity = self.getTotalPop()/self.maxPop

				try:
					newviruses.append(i.reproduce(PopDensity))

				except NoChildException:
					continue
		self.viruses = self.viruses + newviruses			
		return self.getTotalPop()
#
# PROBLEM 2
#

def problem2():
	"""
	Run the simulation and plot the graph for problem 2 (no drugs are used,
	viruses do not have any drug resistance).    

	Instantiates a patient, runs a simulation for 300 timesteps, and plots the
	total virus population as a function of time.    
	"""
	# TODO    
	viruses = []
	for virus_particle in range(100):
		viruses.append(SimpleVirus(0.1,0.05))

	simplepatient = SimplePatient(viruses,1000)

	popvalue = []
	for each in range(300):
		popvalue.append(simplepatient.update())


	print (popvalue)
	pylab.figure()
	pylab.plot(popvalue)
	pylab.ylabel( 'Virus Population' )
	pylab.xlabel( 'Timesteps' )
	pylab.title( 'P2 - Total Virus Population Over Time' )
	pylab.show()

# problem2()
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
	"""
	Representation of a virus which can have drug resistance.
	"""    
	
	def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
		"""
		Initialize a ResistantVirus instance, saves all parameters as attributes
		of the instance.
		
		maxBirthProb: Maximum reproduction probability (a float between 0-1)        
		
		clearProb: Maximum clearance probability (a float between 0-1).
		
		resistances: A dictionary of drug names (strings) mapping to the state
		of this virus particle's resistance (either True or False) to each drug.
		e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
		particle is resistant to neither guttagonol nor grimpex.

		mutProb: Mutation probability for this virus particle (a float). This is
		the probability of the offspring acquiring or losing resistance to a drug.        
		"""
		# TODO
		self.maxBirthProb = maxBirthProb
		self.clearProb = clearProb
		self.resistances = resistances
		self.mutProb = mutProb

	def getResistance(self, drug):
		"""
		Get the state of this virus particle's resistance to a drug. This method
		is called by getResistPop() in Patient to determine how many virus
		particles have resistance to a drug.        

		drug: the drug (a string).

		returns: True if this virus instance is resistant to the drug, False
		otherwise.
		"""
		# TODO
		if self.resistances[drug]:
			return True
		return False 	

		
	def reproduce(self, popDensity, activeDrugs):
		"""
		Stochastically determines whether this virus particle reproduces at a
		time step. Called by the update() method in the Patient class.

		If the virus particle is not resistant to any drug in activeDrugs,
		then it does not reproduce. Otherwise, the virus particle reproduces
		with probability:       
		
		self.maxBirthProb * (1 - popDensity).                       
		
		If this virus particle reproduces, then reproduce() creates and returns
		the instance of the offspring ResistantVirus (which has the same
		maxBirthProb and clearProb values as its parent). 

		For each drug resistance trait of the virus (i.e. each key of
		self.resistances), the offspring has probability 1-mutProb of
		inheriting that resistance trait from the parent, and probability
		mutProb of switching that resistance trait in the offspring.        

		For example, if a virus particle is resistant to guttagonol but not
		grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
		that the offspring will lose resistance to guttagonol and a 90% 
		chance that the offspring will be resistant to guttagonol.
		There is also a 10% chance that the offspring will gain resistance to
		grimpex and a 90% chance that the offspring will not be resistant to
		grimpex.

		popDensity: the population density (a float), defined as the current
		virus population divided by the maximum population        

		activeDrugs: a list of the drug names acting on this virus particle
		(a list of strings). 
		
		returns: a new instance of the ResistantVirus class representing the
		offspring of this virus particle. The child should have the same
		maxBirthProb and clearProb values as this virus. Raises a
		NoChildException if this virus particle does not reproduce.         
		"""
		# # TODO

		for drug in activeDrugs:
			if not self.getResistance(drug):
				raise NoChildException()

		if random.random() <= self.maxBirthProb*(1 - popDensity):
			offspring_resistance = 1 - self.mutProb
			update_resistance = {}
			for drug in self.resistances:
				if random.random() <= offspring_resistance:
					update_resistance[drug] = self.resistances[drug]
				else:
					update_resistance[drug] = not self.resistances[drug]
			return ResistantVirus(self.maxBirthProb, self.clearProb, update_resistance, self.mutProb)

		else:
			raise NoChildException()	




class Patient(SimplePatient):
	"""
	Representation of a patient. The patient is able to take drugs and his/her
	virus population can acquire resistance to the drugs he/she takes.
	"""
	
	def __init__(self, viruses, maxPop):
		"""
		Initialization function, saves the viruses and maxPop parameters as
		attributes. Also initializes the list of drugs being administered
		(which should initially include no drugs).               

		viruses: the list representing the virus population (a list of
		SimpleVirus instances)
		
		maxPop: the  maximum virus population for this patient (an integer)
		"""
		# TODO
		# SimplePatient.__init__(self, viruses,maxPop)
		self.viruses = viruses
		self.maxPop = maxPop
		self.prescription = []
	def addPrescription(self, newDrug):
		"""
		Administer a drug to this patient. After a prescription is added, the 
		drug acts on the virus population for all subsequent time steps. If the
		newDrug is already prescribed to this patient, the method has no effect.

		newDrug: The name of the drug to administer to the patient (a string).

		postcondition: list of drugs being administered to a patient is updated
		"""
		# TODO
		if newDrug not in self.prescription:
			self.prescription.append(newDrug)

	def getPrescriptions(self):
		"""
		Returns the drugs that are being administered to this patient.

		returns: The list of drug names (strings) being administered to this
		patient.
		"""
		# TODO
		return self.prescription

	def getResistPop(self, drugResist):
		"""
		Get the population of virus particles resistant to the drugs listed in 
		drugResist.        

		drugResist: Which drug resistances to include in the population (a list
		of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

		returns: the population of viruses (an integer) with resistances to all
		drugs in the drugResist list.
		"""
		# TODO
		resistpop = 0
		for virus in self.viruses:
			resist_all = 0
			for drug in drugResist:
				if virus.getResistance(drug):
					resist_all += 1
				else:
					resist_all = 0
			resistpop = resistpop + resist_all

		return resistpop
				
	def update(self):
		"""
		Update the state of the virus population in this patient for a single
		time step. update() should execute these actions in order:

		- Determine whether each virus particle survives and update the list of 
		  virus particles accordingly
		  
		- The current population density is calculated. This population density
		  value is used until the next call to update().

		- Determine whether each virus particle should reproduce and add
		  offspring virus particles to the list of viruses in this patient. 
		  The listof drugs being administered should be accounted for in the
		  determination of whether each virus particle reproduces. 

		returns: the total virus population at the end of the update (an
		integer)
		"""
		# TODO
		newviruses = []
		for i in self.viruses:
			if i.doesClear():
				self.viruses.remove(i)	
			else: 
				PopDensity = self.getTotalPop()/self.maxPop

				try:
					newviruses.append(i.reproduce(PopDensity, self.prescription))

				except NoChildException:
					continue
		self.viruses = self.viruses + newviruses
		return self.getTotalPop()


# PROBLEM 4
#

def problem4():
	"""
	Runs simulations and plots graphs for problem 4.

	Instantiates a patient, runs a simulation for 150 timesteps, adds
	guttagonol, and runs the simulation for an additional 150 timesteps.

	total virus population vs. time  and guttagonol-resistant virus population
	vs. time are plotted
	"""
	# TODO
	viruspopulation = 100
	maxPop = 1000
	maxBirthProb = 0.1
	clearProb = 0.05
	resistances = {'guttagonol': False}
	mutProb = 0.005
	timesteps = 300


	# initiating list containing 100 virus instances
	viruses = []
	for particle in range(viruspopulation):
		viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))


	# initiating Patient instance
	patient = Patient(viruses, maxPop)

	# initiating list containing virus population per timestep
	popvalue = []
	# initiating a list containing virus population resistant to the drug per timestep
	guttagonol_resistant = []
	for each in range(timesteps):
		popvalue.append(patient.update())
		guttagonol_resistant.append(patient.getResistPop(['guttagonol']))
		if each == 150:
			patient.addPrescription('guttagonol')

	pylab.figure()
	pylab.plot( popvalue, label = 'virus population')
	pylab.plot( guttagonol_resistant, label = 'guttagonol resistance')
	pylab.ylabel( 'Virus Population' )
	pylab.xlabel( 'Timesteps' )
	pylab.title('P4 - Total Virus Population Over Time' )
	pylab.legend(loc = 2)
	pylab.show()

# problem4()

# The virus population shows an increasing trend till about 150 timesteps. Till this point, the number of
# virus particles resistant to guttagonol is fairly low through mutation. After the introduction of the
# drug, the virus population dramatically plummets till the number of particles resistant to guttagonol relative
# to the total virus population is a sufficiently significant number. After this point, the virus population increases
# due to higher presence of guttagonol resistant virus particles in the patient. Due to this, there is a similar
# increase in the number of guttagonol-resistant virus particle.

# This trend is largely consistent with my intuition. The only aspect was that the final virus population suprisingly 
# stabilizes at a rate roughly similar to that around 150 timesteps (before guttagonol intro) . As the development of resistant 
#trait during mutation is stochastically determined, I would've expected the virus population to stabilize at a lower rate

#
# PROBLEM 5
#
		
def problem5():
# 	"""
# 	Runs simulations and make histograms for problem 5.

# 	Runs multiple simulations to show the relationship between delayed treatment
# 	and patient outcome.

# 	Histograms of final total virus populations are displayed for delays of 300,
# 	150, 75, 0 timesteps (followed by an additional 150 timesteps of
# 	simulation).    
# 	"""
# # 	# TODO


	# A function desgined to return the final total virus population in a patient with
	# lag time between administration of the drug as the argument.
	def testpatient(timesteps):
		viruspopulation = 100
		maxPop = 1000
		maxBirthProb = 0.1
		clearProb = 0.05
		resistances = {'guttagonol': False}
		mutProb = 0.005
		total_timesteps = timesteps + 400


		# initiating list containing 100 virus instances
		viruses = []
		for particle in range(viruspopulation):
			viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

		# initiating Patient instance
		patient = Patient(viruses, maxPop)

		for each in range(total_timesteps):
			totalviruspop = patient.update()
			if each == timesteps:
				patient.addPrescription('guttagonol')

		return totalviruspop


	# a list containing the lag time before administration of the drug
	lag_time = [0, 150, 75, 300]
	for timesteps in lag_time:
		print('timesteps till treatment', timesteps)
		patientscured = 0
		finalviruspop = []
		patientcount = 500
		for each in range(patientcount):
			finalviruspop.append(testpatient(timesteps))
			if finalviruspop[-1] <= 50:
				patientscured += 1
		print('my final virus pop', finalviruspop)		
		print('% patients cured is', float((patientscured)/float(patientcount))*100)

		pylab.figure()
		pylab.hist(finalviruspop)
		pylab.ylabel( ' Number of Patients' )
		pylab.xlabel( 'Final Virus Population')
		pylab.title( 'P5 - Histograms of final virus populations displayed for delays of %i timesteps.' % timesteps )
		pylab.show()


# problem5()

# Number of trials conducted for each of the four conditions was 500. I.e., on 500 patients. This was considered to be a good
# representative of the broader outcome. The trial was initially tested on 30 patients and was gradually increased to
# observe consistency. The results were consistent across differnt trial numbers through till larger numbers in the hundreds.
# Thus, 500 was considerered to be a sufficient number of trials and is roughly in line with real word trials numbers for initial drug testing

# 1. For the first simulation with lag time of 300, less than 2% of patients were in recovery

# 2. For the second simulation with lag time of 150, less than 4% of patients were in recovery which is close to the first simulation.

# 3. For the third simulation with lag time of 75, about 15% of the patients were in recovery

# 4. For the fourth simulation with lag time of 0, about 98% of the patients were in recovery. 

# For the above three simulations, as the virus population consistently increase before the introduction of the drug, 
# there is negative correlation between the lag time and the number of patients in recovery . If the drug is
# introduced at a much later stage when the population has grown, a higher number of particles will gain resistant
# to the drug. As a result, the final virus population reaches a rate higher which is than the remission rate

# Thus, for the last simulation, as the drug is introduced at the very first timestep since the introduction
# of the first set of virus population, the particles do not get a chance to reproduce at all and the
# with every subsequent timestep, the population plummets.
	
#
# PROBLEM 6
#

def problem6():
	"""
	Runs simulations and make histograms for problem 6.

	Runs multiple simulations to show the relationship between administration
	of multiple drugs and patient outcome.
	
	Histograms of final total virus populations are displayed for lag times of
	150, 75, 0 timesteps between adding drugs (followed by an additional 150
	timesteps of simulation).
	"""
	# # TODO
	# A function desgined to return the final total virus population in a patient with
	# lag time between the administrating the drugs as the argument.	
	def testpatient(timesteps):
		viruspopulation = 100
		maxPop = 1000
		maxBirthProb = 0.1
		clearProb = 0.05
		resistances = {'guttagonol': False, 'grimpex': False}
		mutProb = 0.005
		total_timesteps = timesteps + 301

		# initiating list containing 100 virus instances
		viruses = []
		for particle in range(viruspopulation):
			viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))


		# initiating Patient instance
		patient = Patient(viruses, maxPop)

		for each in range(total_timesteps):
			totalviruspop = patient.update()
			if each == 150:
				patient.addPrescription('guttagonol')
			if each ==(timesteps+150):
				patient.addPrescription('grimpex')
		

		return totalviruspop


	# a list containing the lag times between between the administration of the drugs  
	lagtime_secondtreatment = [300, 150, 75, 0]
	for timesteps in lagtime_secondtreatment:
		print('timesteps till second treatment', timesteps)
		patientscured = 0
		finalviruspop = []
		patientcount = 30
		for each in range(patientcount):
			finalviruspop.append(testpatient(timesteps))
			if finalviruspop[-1] <= 50:
				patientscured += 1
		print('my final virus pop', finalviruspop)		
		print('% patients cured is', float((patientscured)/float(patientcount))*100)



		pylab.figure()
		pylab.hist( finalviruspop )
		pylab.ylabel( 'Number Of patients' )
		pylab.xlabel( 'Final Virus Population')
		pylab.title( 'P6 - Histograms of final virus populations displayed for lag times of %i timesteps between adding drugs.' % timesteps )
		pylab.show()

# problem6()


# 1. For the first simulation with lag time of 300, less than 3.5% of patients were in recovery

# 2. For the second simulation with lag time of 150, less than 14% of patients were in recovery 

# 3. For the third simulation with lag time of 75, about 54% of the patients were in recovery

# 4. For the fourth simulation with lag time of 0, about 97% of the patients were in recovery. 

# We obersve that there is a negative correlation between the lag time between the administration of
# the drugs and the final virus populations in the patients. As with the previous problem, the longer
# the time between the adminsitration of the drugs, higher number of virus particles reproduce and 
# develop resistance against the drugs

# However, larger number of patients are in recovery in the second and third simulations compared
# to problem 5 solution. This might be because of the fact that there are multiple drugs acting
# independently on the patient to fight against the virus. 

# PROBLEM 7
# #
	 
def problem7():
# 	"""
# 	Run simulations and plot graphs examining the relationship between
# 	administration of multiple drugs and patient outcome.

# 	Plots of total and drug-resistant viruses vs. time are made for a
# 	simulation with a 300 time step delay between administering the 2 drugs and
# 	a simulations for which drugs are administered simultaneously.        
# 	"""
# 	# TODO
	def helperfunction(lagtime):
		viruspopulation = 100
		maxPop = 1000
		maxBirthProb = 0.1
		clearProb = 0.05
		resistances = {'guttagonol': False, 'grimpex': False}
		mutProb = 0.005
		timesteps = lagtime + 301


		# initiating list containing 100 virus instances
		viruses = []
		for particle in range(viruspopulation):
			viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))


		# initiating Patient instance
		patient = Patient(viruses, maxPop)

		# initiating list containing virus population per timestep
		popvalue = []
		# initiating a list containing virus population resistant to guttagonol per timestep
		guttagonol_resistant = []

		# initiating a list containing virus population resistant to grimpex per timestep
		grimpex_resistant  = []
		for each in range(timesteps):
			popvalue.append(patient.update())
			guttagonol_resistant.append(patient.getResistPop(['guttagonol']))
			grimpex_resistant.append(patient.getResistPop(['grimpex']))
			if each == 150:
				patient.addPrescription('guttagonol')
			if each	== (lagtime + 150):
				patient.addPrescription('grimpex')

		return popvalue, guttagonol_resistant, grimpex_resistant		

	lagtime_secondtreatment = [300, 0]
	for timesteps in lagtime_secondtreatment:
		print('lag time between treatment', timesteps)
		popvalue, guttagonol_resistant, grimpex_resistant = helperfunction(timesteps)

		print('virus population over time', popvalue) 
		print('virus population resistant to guttagonol over time', guttagonol_resistant)
		print('virus population resistant to grimpex over time', grimpex_resistant)


		pylab.figure()
		pylab.plot( popvalue, label = 'virus population')
		pylab.plot( guttagonol_resistant, label = 'guttagonol resistance')
		pylab.plot( grimpex_resistant, label = 'grimpex resistance')		
		pylab.ylabel( 'Virus Population' )
		pylab.xlabel( 'Timesteps' )
		pylab.title('P7 - Total Virus Population Over Time' )
		pylab.legend(loc = 3)
		pylab.show()


# problem7()




# Problem 8 - For such a scenario, we can add a variable to Patient Class which equals the probability that
# the patient will take the drugs. This probabiltiy can be determined by analysing historical real world data 
# on patient non-compliance with taking drugs. Subsequently, in the add prescription method, we can stochastically
# determine whether the patient will take the drug against this fixed probability at a particular timestep.