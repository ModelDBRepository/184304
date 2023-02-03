'''
Defines a class, Neuron472451419, of neurons from Allen Brain Institute's model 472451419

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472451419:
    def __init__(self, name="Neuron472451419", x=0, y=0, z=0):
        '''Instantiate Neuron472451419.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472451419_instance is used instead
        '''
                
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Nr5a1-Cre_Ai14_IVSCC_-177334.05.01.01_471120787_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon

        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472451419_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 63.36
            sec.e_pas = -99.7316513062
        for sec in self.apic:
            sec.cm = 7.54
            sec.g_pas = 1.53841275591e-05
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000323547761688
        for sec in self.dend:
            sec.cm = 7.54
            sec.g_pas = 6.04961563626e-06
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.0079231
            sec.gbar_Ih = 8.61267e-06
            sec.gbar_NaTs = 0.831809
            sec.gbar_Nap = 0.000115828
            sec.gbar_K_P = 0.0198868
            sec.gbar_K_T = 6.5088e-05
            sec.gbar_SK = 0.000797996
            sec.gbar_Kv3_1 = 0.0281648
            sec.gbar_Ca_HVA = 2.69146e-05
            sec.gbar_Ca_LVA = 0.000783165
            sec.gamma_CaDynamics = 0.0264831
            sec.decay_CaDynamics = 739.8
            sec.g_pas = 0.000153169
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

