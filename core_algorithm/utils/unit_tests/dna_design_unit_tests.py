import unittest
from core_algorithm.utils.make_eugene_script import *
from core_algorithm.utils.dna_design import *
from core_algorithm.utils.py4j_gateway.gateway import start_gateway
from py4j.java_gateway import JavaGateway


class UnitTests(unittest.TestCase):
    # NOTE: setup fixture for launching miniEugene?
    # @unittest.expectedFailure
    # def setUp(self):
    #     start_gateway()
        #
        # try:
        #     gateway = JavaGateway(eager_load=True)
        #     print("\nJava Py4J gateway already started")
        # except Exception:
        #     print("\nAttempting to start Java Py4J gateway...")
        #     try:
        #         start_gateway()
        #         print("Started Java Py4J gateway")
        #     except Exception:
        #         print("Failed to start Java Py4J gateway!")

    def outputsTest(self, first, second):
        with self.subTest():
            self.assertEqual(first, second)

    def sideEffectsTest(self, first, second):
        pass

    def warningsTest(self, callable, arg):
        with self.subTest():
            self.assertWarns(Warning, callable, arg)


class SubTests(UnitTests):

    # Test Auxiliary Functions
    def test_hex_to_rgb(self):
        self.outputsTest(hex_to_rgb('000000'), '0.0;0.0;0.0')
        self.outputsTest(hex_to_rgb('FFFFFF'), '1.0;1.0;1.0')     # rgb: 255;255;255
        self.outputsTest(hex_to_rgb('3badb8'), '0.23;0.68;0.72')  # rgb: 59;173;184
        self.warningsTest(hex_to_rgb, '')
        self.warningsTest(hex_to_rgb, 'blah')
        self.warningsTest(hex_to_rgb, 123456)

    # Test DNADesign Methods
    def test_get_part_orders(self):
        structs = {'Gate3': EugeneStruct(type='gate', gates_name='Gate3', gates_group='M3', gates_model='Gate3_model', gates_struct='Gate3_structure', struct_cassettes=[['Gate3_a', 'Gate3_a_cassette', 1, ['M3', 'ECK120034435']], ['Gate3_b', 'Gate3_b_cassette', 1, ['M3', 'ECK120034435']]], inputs=['IPTG_sensor'], outputs=['PM3'], color='8FC73E'), 'IPTG_sensor': EugeneStruct(type='input', gates_name='IPTG_sensor', gates_group='', gates_model='IPTG_sensor_model', gates_struct='IPTG_sensor_structure', struct_cassettes=[], inputs=[], outputs=['P_IPTG'], color=''), 'Gate1': EugeneStruct(type='gate', gates_name='Gate1', gates_group='M1', gates_model='Gate1_model', gates_struct='Gate1_structure', struct_cassettes=[['Gate1_a', 'Gate1_a_cassette', 1, ['M1', 'L3S3P41']], ['Gate1_b', 'Gate1_b_cassette', 1, ['M1', 'L3S3P41']]], inputs=['aTc_sensor'], outputs=['PM1'], color='3BA9E0'), 'aTc_sensor': EugeneStruct(type='input', gates_name='aTc_sensor', gates_group='', gates_model='aTc_sensor_model', gates_struct='aTc_sensor_structure', struct_cassettes=[], inputs=[], outputs=['P_aTc'], color=''), 'Gate5': EugeneStruct(type='gate', gates_name='Gate5', gates_group='M5', gates_model='Gate5_model', gates_struct='Gate5_structure', struct_cassettes=[['Gate5_a', 'Gate5_a_cassette', 1, ['M5', 'ECK125109870']], ['Gate5_b', 'Gate5_b_cassette', 1, ['M5', 'ECK125109870']]], inputs=['Gate3', 'Gate1'], outputs=['PM5'], color='5455A4'), 'nanoluc_reporter_2': EugeneStruct(type='output', gates_name='nanoluc_reporter_2', gates_group='', gates_model='nanoluc_reporter_2_model', gates_struct='nanoluc_reporter_2_structure', struct_cassettes=[['nanoluc_reporter_2_a', 'nanoluc_cassette', 1, ['nanoluc_cassette']], ['nanoluc_reporter_2_b', 'nanoluc_cassette', 1, ['nanoluc_cassette']]], inputs=['Gate5'], outputs='', color='')}
        cassettes = {'Gate3_a': EugeneCassette(struct_var_name='Gate3_a', struct_cas_name='Gate3_a_cassette', type='gate', inputs=['P_IPTG'], comps=['M3', 'ECK120034435'], outputs=['PM3'], color='8FC73E', dev_rules=['ALL_FORWARD'], cir_rules=[]), 'Gate1_a': EugeneCassette(struct_var_name='Gate1_a', struct_cas_name='Gate1_a_cassette', type='gate', inputs=['P_aTc'], comps=['M1', 'L3S3P41'], outputs=['PM1'], color='3BA9E0', dev_rules=['ALL_FORWARD'], cir_rules=[]), 'Gate5_a': EugeneCassette(struct_var_name='Gate5_a', struct_cas_name='Gate5_a_cassette', type='gate', inputs=['PM3'], comps=['M5', 'ECK125109870'], outputs=['PM5'], color='5455A4', dev_rules=['ALL_FORWARD'], cir_rules=[]), 'Gate5_b': EugeneCassette(struct_var_name='Gate5_b', struct_cas_name='Gate5_b_cassette', type='gate', inputs=['PM1'], comps=['M5', 'ECK125109870'], outputs=['PM5'], color='5455A4', dev_rules=['ALL_FORWARD'], cir_rules=[]), 'nanoluc_reporter_2_a': EugeneCassette(struct_var_name='nanoluc_reporter_2_a', struct_cas_name='nanoluc_cassette', type='output', inputs=['PM5'], comps=['nanoluc_cassette'], outputs='', color='', dev_rules=['ALL_FORWARD'], cir_rules=[])}
        sequences = {'P_IPTG': EugeneSequence(parts_type='promoter', parts_name='P_IPTG', parts_sequence='TTACAAAGAAAATTCGACAAACTGTTATTTTTCTATCTATTTATTTGAATTGTGAGCGGATAACAATTACCTTTGTCGGCAATTGTGAGCGGATAACAATTAAATAAAGATATTCTCGTCAAACAAATATAAATAATATAAAC', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'P_aTc': EugeneSequence(parts_type='promoter', parts_name='P_aTc', parts_sequence='ttttgcacccgctttccaagagaagaaagccttgttaaattgacttagtgtaaaagcgcagtactgcttgaccataagaacaaaaaaatctctatcactgatagggataaagtttggaagataaagctaaaagttcttatctttgcagtctccctatcagtgatagagacgca', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'M1': EugeneSequence(parts_type='cds', parts_name='M1', parts_sequence='CAAAGATAATAGAACTTAAGGTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTTTT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'L3S3P41': EugeneSequence(parts_type='terminator', parts_name='L3S3P41', parts_sequence='GGATCCAAAAAAAAAAAACACCCTAACGGGTGTTTTTTTTTTTTTGGTCTGCCgcggccgc', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'PM1': EugeneSequence(parts_type='promoter', parts_name='PM1', parts_sequence='TGCTGTCATAGGCCGGTTGTCCGGTAGTCCGGATGATTTAAGGAAGATTTCTCTTCTTTTTTCACTTTCTCCGAACAACCTCCACTTAAGTTCTATTATCTTTGCAGT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'M3': EugeneSequence(parts_type='cds', parts_name='M3', parts_sequence='CAAAGATAATTAAGTTAAGGGTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTTTT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'ECK120034435': EugeneSequence(parts_type='terminator', parts_name='ECK120034435', parts_sequence='GGATCCCTCGGTACCAAATTCCAGAAAAGAGACGCTGAAAAGCGTCTTTTTTCGTTTTGGTCCgcggccgc', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'PM3': EugeneSequence(parts_type='promoter', parts_name='PM3', parts_sequence='TGCTGTCATAGGCCGGTTGTCCGGTAGTCCGGATGATTTAAGGAAGATTTCTCTTCTTTTTTCACTTTCTCCGAACAACCTCCACCTTAACTTAATTATCTTTGCAGT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'M5': EugeneSequence(parts_type='cds', parts_name='M5', parts_sequence='CAAAGATAGAATAAGTCTTTGTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTTTT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'ECK125109870': EugeneSequence(parts_type='terminator', parts_name='ECK125109870', parts_sequence='ccaattattgAACACCCTAACGGGTGTTTTTTTGTTTctggtctccc', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'PM5': EugeneSequence(parts_type='promoter', parts_name='PM5', parts_sequence='TGCTGTCATAGGCCGGTTGTCCGGTAGTCCGGATGATTTAAGGAAGATTTCTCTTCTTTTTTCACTTTCTCCGAACAACCTCCAAAAGACTTATTCTATCTTTGCAGT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'F_scar': EugeneSequence(parts_type='scar', parts_name='F_scar', parts_sequence='CGCT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'E_scar': EugeneSequence(parts_type='scar', parts_name='E_scar', parts_sequence='GCTT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'D_scar': EugeneSequence(parts_type='scar', parts_name='D_scar', parts_sequence='AGGT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'C_scar': EugeneSequence(parts_type='scar', parts_name='C_scar', parts_sequence='AATG', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'B_scar': EugeneSequence(parts_type='scar', parts_name='B_scar', parts_sequence='TACG', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'A_scar': EugeneSequence(parts_type='scar', parts_name='A_scar', parts_sequence='GGAG', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'Y_scar': EugeneSequence(parts_type='scar', parts_name='Y_scar', parts_sequence='ATTG', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'X_scar': EugeneSequence(parts_type='scar', parts_name='X_scar', parts_sequence='TGTC', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'V_scar': EugeneSequence(parts_type='scar', parts_name='V_scar', parts_sequence='TCTG', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'U_scar': EugeneSequence(parts_type='scar', parts_name='U_scar', parts_sequence='GGGC', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'R_scar': EugeneSequence(parts_type='scar', parts_name='R_scar', parts_sequence='GTAA', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'Q_scar': EugeneSequence(parts_type='scar', parts_name='Q_scar', parts_sequence='GAGT', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'P_scar': EugeneSequence(parts_type='scar', parts_name='P_scar', parts_sequence='CCTA', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'O_scar': EugeneSequence(parts_type='scar', parts_name='O_scar', parts_sequence='ATGC', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'G_scar': EugeneSequence(parts_type='scar', parts_name='G_scar', parts_sequence='ATAG', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000'), 'nanoluc_cassette': EugeneSequence(parts_type='cassette', parts_name='nanoluc_cassette', parts_sequence='ATGGTTTTTACTCTGGAAGATTTTGTTGGCGATTGGCGTCAGACCGCGGGTTATAATTTGGATCAAGTCCTGGAACAGGGTGGCGTAAGCTCTCTGTTCCAGAACCTGGGTGTGAGCGTGACGCCGATTCAGCGCATCGTTCTGTCCGGCGAGAACGGTCTGAAAATTGATATTCATGTGATCATCCCGTACGAAGGCCTGAGCGGTGACCAAATGGGTCAAATCGAGAAAATCTTTAAAGTCGTCTACCCAGTTGACGATCACCACTTCAAGGTTATCTTGCATTACGGTACGCTGGTGATTGATGGTGTGACCCCGAATATGATTGACTATTTCGGCCGTCCGTATGAAGGCATTGCCGTTTTTGACGGTAAAAAGATCACCGTCACCGGTACCCTGTGGAATGGCAATAAGATTATTGACGAGCGTCTGATTAACCCGGACGGCAGCCTGCTGTTCCGCGTGACCATCAACGGTGTCACGGGTTGGCGTCTGTGCGAGCGCATCCTGGCATAA', dev_rules=['ALL_FORWARD'], cir_rules=[], color='000000')}
        device_rules = ['ALL_FORWARD']
        circuit_rules = ['ALL_FORWARD', 'STARTSWITH L1', 'ENDSWITH L2', 'Gate5_a AFTER Gate3_a', 'Gate5_a AFTER Gate1_a', 'Gate3_a AFTER Gate1_a', 'CONTAINS Gate3_a', 'CONTAINS Gate1_a', 'CONTAINS Gate5_a', 'CONTAINS Gate5_b', 'CONTAINS nanoluc_reporter_2_a']
        fenceposts = {'L1': [], 'L2': []}
        dna_designs = DNADesign(structs, cassettes, sequences, device_rules, circuit_rules, fenceposts)
        dna_designs.prep_to_get_part_orders()
        circuit_rules_target = ['ALL_FORWARD', 'STARTSWITH L1', 'ENDSWITH L2', 'Gate5_a AFTER Gate3_a', 'Gate5_a AFTER Gate1_a', 'Gate3_a AFTER Gate1_a', 'CONTAINS Gate3_a', 'CONTAINS Gate1_a', 'CONTAINS Gate5_a', 'CONTAINS Gate5_b', 'CONTAINS nanoluc_reporter_2_a', 'CONTAINS L1', 'CONTAINS L2']
        self.outputsTest(dna_designs.circuit_rules, circuit_rules_target)
        mini_eugene_part_orders = dna_designs.get_part_orders()  # Calls miniEugene
        print(mini_eugene_part_orders)


if __name__ == '__main__':
    unittest.main()
