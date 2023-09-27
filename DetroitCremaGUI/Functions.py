import Setups as s
import pandas as pd

def Heat_Up():
	print("Heating Up!")
	s.sol.value = True
	while s.pressure < 10:
		s.pressure = s.raw_pressure = (((s.chan.value*.000125) - .506)*4)
		#print(s.pressure)
		s.pumpOn = True
	s.pumpOn = False
	s.endTime = s.time.time() + (180)
	s.startTime = s.time.time()
	s.heat_up_flag = True
	while s.heat_up_flag is True:
		if s.loops > 10:
			#print('Temp: {}  CPS: {}  Elap Time: {}'.format(s.temp_list[s.loops-1], s.cps_T, s.elapsedTime))
			s.temp = s.thermocouple.temperature
			Set_CPS_T()
			s.elapsedTime = s.time.time() - s.startTime
			s.temp_list.append(s.temp)
			s.elapsedTime_list.append(s.elapsedTime)
			while s.click < 100:
				if s.counter < s.cps_T:
					s.rel.value = True
				else:
					s.rel.value = False	
				s.counter+=1
				s.click+=1
				
			s.counter = 0
			s.click = 0
			s.loops += 1
			print(s.temp)
		if s.loops <= 10:
			s.temp = s.thermocouple.temperature
			s.temp_list.append(s.temp)
			s.elapsedTime = s.time.time() - s.startTime
			s.elapsedTime_list.append(s.elapsedTime)
			s.loops += 1
			#print('loops under 10')
	s.pumpOn = False
	
def Purge():
	purge_time = s.time.time() + 5
	s.rel.value = False
	while s.time.time() < purge_time:
		Maintain_Temp()
		s.pumpOn = True
	s.pumpOn = False
	
def Infuse():
	s.infuse_flag = True
	while s.temp < s.targ_temp:
		if s.loops > 10:
			s.temp = s.thermocouple.temperature
			Set_CPS_T()
			s.elapsedTime = s.time.time() - s.startTime
			s.temp_list.append(s.temp)
			s.elapsedTime_list.append(s.elapsedTime)
			while s.click < 100:
				if s.counter < s.cps_T:
					s.rel.value = True
				else:
					s.rel.value = False	
				s.counter+=1
				s.click+=1
				
			s.counter = 0
			s.click = 0
			s.loops += 1
			print(s.temp)
	
	loop_start = 0
	s.temp_list.clear()
	s.elapsedTime_list.clear()
	s.loops = 0
	temp = s.Thread(target = Get_Temp)
	temp.start()
	s.sol.value = False
	s.prev_loop_time = s.time.time()
	Begin_Timer()
	while s.time.time() <= s.endTime:
		Maintain_Temp()
		loop_start = s.time.time()
		Get_Pressure()
		Get_Weight()
		Set_CPS_P()
		Set_CPS_T()
		s.elapsedTime = s.time.time() - s.startTime
		Append_Lists()
		s.loop_end += s.time.time() - loop_start
		while s.click < 100:  
			if s.counter < s.cps:
				s.pumpOn = True
			else:
				s.pumpOn = False
				
			if s.counter < s.cps_T:
				s.rel.value = True
			else:
				s.rel.value = False
				
			
			s.counter+=1
			s.click+=1
		s.counter = 0
		s.click = 0
		s.loops += 1
	print('Avg loop time: {}'.format(s.loop_end/s.loops))
	Retrieve_Data()
	
def Get_Temp():
	k = 0
	while s.time.time() < s.endTime:
		try:
			s.temp = s.thermocouple.temperature
			k += 1
		except:
			pass	
	
def Get_Weight():
	try:
		w = (s.hx.get_value(1)/s.raw_to_gram)
		if w > s.weight_list[s.loops-1] + 1:
			w = s.weight_list[s.loops-1] + 1
		if w < s.weight_list[s.loops-1] - 1:
			w = s.weight_list[s.loops-1] - 1
		s.weight = (s.np.exp(-.105)*s.weight_list[s.loops-1] + w*.1)
		print(s.weight)
	except:
		s.weight = 0 
				
def Maintain_Temp():
	Set_CPS_T()
	if s.cps_T > 100:
		s.cps_T = 100
	if s.cps_T <= 0:
		s.cps_T = 1
		
def Get_Pressure():
	print('Loops is: {}'.format(s.loops))
	if s.loops > 0:
		s.raw_pressure = (((s.chan.value*.000125) - .506)*4)
		#s.pressure = s.np.exp(-.02)*s.pressure_list[s.loops-1]+.02*s.raw_pressure
		s.pressure = s.np.exp(-.02)*s.prev_pressure +.02*s.raw_pressure
		s.prev_pressure = s.pressure
	else:
		s.pressure = (((s.chan.value*.000125) - .506)*4)
		s.prev_pressure = s.pressure
					
def Set_CPS_P():
	s.cps = PD_CPS(s.cps)
	if s.cps > 100:
		s.cps = 100
	if s.cps <= 0:
		s.cps = 1

def Set_CPS_T():
	s.cps_T = PD_Temp(s.cps_T)
	if s.cps_T > 100:
		s.cps_T = 100
	if s.cps_T <= 0:
		s.cps_T = 1
		
def PD_CPS(cps):
	kp = 1.9
	kd = .4
	delta_t = s.time.time() - s.prev_loop_time_P
	try:
		pd_dot = (s.profile.getPressureTarg(s.elapsedTime + delta_t) - s.profile.getPressureTarg(s.elapsedTime))/delta_t
		p_dot = (s.pressure - s.pressure_list[s.loops - 1])/delta_t
		e = s.profile.getPressureTarg(s.elapsedTime) - s.pressure
		e_dot = pd_dot - p_dot
		s.delta_cps = (kp*e) + (kd*e_dot)
		new_cps = cps + s.delta_cps
		s.prev_loop_time_P = s.time.time()
		return new_cps
	except:
		s.prev_loop_time_P = s.time.time()
		return s.cps
		
def PD_Temp(cps_T):
	if s.heat_up_flag is True:
		kp = 6
		kd = 12
	else:
		kp = 6
		kd = 12
	delta_t = .09 # 90 ms sampling rate
	try:
		pd_dot = 0
		p_dot = (s.temp - s.temp_list[s.loops - 1])/delta_t
		e = s.targ_temp - s.temp
		e_dot = pd_dot - p_dot
		s.delta_cps_T = (kp*e) + (kd*e_dot)
		new_cps = cps_T + s.delta_cps_T
		return new_cps 
	except:
		return s.cps_T
		
def Append_Lists():
	s.weight_list.append(s.weight)
	if s.elapsedTime < s.profile.time.max():
		s.expected_pressure_list.append(s.profile.getPressureTarg(s.elapsedTime))
	s.pressure_list.append(s.pressure)
	s.raw_pressure_list.append(s.raw_pressure)
	s.cps_list.append(s.cps)
	s.cps_temp_list.append(s.cps_T)
	s.delta_cps_list.append(s.delta_cps) 
	s.delta_cps_list_T.append(s.delta_cps_T)
	s.elapsedTime_list.append(s.elapsedTime)
	s.temp_list.append(s.temp)
	#print(s.elapsedTime, s.weight)
def Retrieve_Data():
	dict = {'Temp': s.temp_list, 'Elapsed Time': s.elapsedTime_list}
	df = pd.DataFrame(dict)
	df.to_csv('/home/centrepolis/Desktop/Temp CSV/test1.csv')
	
def Begin_Timer():
	s.startTime = s.time.time()
	#s.preinfuseTime = s.time.time() + preInfuseTime
	s.endTime = s.time.time() + s.profile.time.max()
