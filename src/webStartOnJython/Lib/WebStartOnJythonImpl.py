import sys
# this is essential, otherwise 'os' import will not work
sys.path.append('__pyclasspath__/Lib')


# from javax.net.ssl import TrustManager, X509TrustManager
# from jarray import array
# from javax.net.ssl import SSLContext


# # Turn off certificate validation
# class TrustAllX509TrustManager(X509TrustManager):
#     '''Define a custom TrustManager which will blindly accept all certificates'''
#     def checkClientTrusted(self, chain, auth):
#         pass

#     def checkServerTrusted(self, chain, auth):
#         pass

#     def getAcceptedIssuers(self):
#         return None
# # Create a static reference to an SSLContext which will use
# # our custom TrustManager
# trust_managers = array([TrustAllX509TrustManager()], TrustManager)
# TRUST_ALL_CONTEXT = SSLContext.getInstance("SSL")
# TRUST_ALL_CONTEXT.init(None, trust_managers, None)
# # Keep a static reference to the JVM's default SSLContext for restoring
# # at a later time
# DEFAULT_CONTEXT = SSLContext.getDefault()
# SSLContext.setDefault(TRUST_ALL_CONTEXT)


from webStartOnJython.interfaces import JySwingType

from javax.swing import JOptionPane

import com.xhaus.jyson.JysonCodec as json


class WebStartOnJythonImpl(JySwingType, object):
    def start(self, args):
        print 'Starting Python with args: %s' % args

        serialized = json.dumps({'hello': 'world'})

        JOptionPane.showMessageDialog(None, "Hello world: %s" % serialized)
