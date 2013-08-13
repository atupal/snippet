import ping, threading, time, socket, select, sys, struct, logging
import binascii, threading, collections, math, random
import ping, ping_server, ping_disk, ping_reporter
import random

log = ping_reporter.setup_log('PingRaid')

class PingRaid():
	def __init__(self, servers):
		self.disks = []
		for host in servers:
			try:
				disk = ping_disk.PingDisk(host)
			except:
				log.error('failed setup: %s'%host)
				continue
			self.disks.append(disk)
		if len(self.disks) == 0:
			raise Exception('PingRaid: no valid servers registered')

	def stop(self):
		for disk in self.disks:
			disk.stop()

	def size(self):        return min([x.size() for x in self.disks])
	def block_size(self):  return min([x.block_size() for x in self.disks])
	def region_size(self): return min([x.region_size() for x in self.disks])
	def get_disk(self):    return random.choice(self.disks)

	def get_region(self, size):
		return self.get_disk().get_region(size)

	def test_region(self, start, cursize, endsize):
		return self.get_disk().test_region(start, cursize, endsize)

	def write(self, index, data):
		for disk in self.disks:
			disk.write(index,data)

	def delete(self, index, length):
		for disk in self.disks:
			disk.delete(index,length)

	def read(self, index, length):
		return self.get_disk().read(index,length)

	def read_min(self, index, length):
		return self.get_disk().read_min(index,length)
