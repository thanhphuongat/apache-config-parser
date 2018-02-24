import unittest
import config_parser

class TestConfigParser(unittest.TestCase):
    def test_paser_nodes(self):
        source = '''# This is comment node
        Listen 80
        <VirtualHost "*:80">
            ServerName localhost
            DocumentRoot /srv/www
        </VirtualHost>
        '''
        conf = config_parser.ApacheConfParser(source, False)
        
        self.assertEqual(len(conf.nodes), 4)
        self.assertIsInstance(conf.nodes[0], config_parser.CommentNode)
        self.assertIsInstance(conf.nodes[1], config_parser.Directive)
        self.assertIsInstance(conf.nodes[2], config_parser.Directive)
        self.assertIsInstance(conf.nodes[3], config_parser.BlankNode)

        vhost = conf.nodes[2]
        self.assertSequenceEqual(vhost.arguments, ['"*:80"'])
        self.assertEqual(len(vhost.body.nodes), 2)

