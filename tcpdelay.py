
from optparse import OptionParser
from twisted.internet import reactor
from delayforward import ProxyFactory

parser = OptionParser("Usage %prog [options] arg\n\nExample:\npython %prog -H yandex.ru -p 80 -d 5")
parser.add_option('-H', '--host', dest = 'host', action = 'store')
parser.add_option('-p', '--port', dest = 'port', action = 'store', type = 'int')
parser.add_option('-l', '--listen', dest='listen', action = 'store', type = 'int')
parser.add_option('-d', '--delay', dest = 'delay', action = 'store', type = 'float')
(options, args) = parser.parse_args()
 
reactor.listenTCP(options.listen, ProxyFactory(options.host, options.port, options.delay));

reactor.run()
