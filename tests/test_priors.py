
from delight.priors import *
from scipy.misc import derivative

NREPEAT = 10


def test_schechter_derivatives():
    """
    Numerically test derivatives of Schechter distribution
    one by one for a few random parameters and values
    """
    for i in range(NREPEAT):
        ellStar = np.random.uniform(low=0., high=10.0, size=1)
        ell = np.random.uniform(low=0., high=10.0, size=1)
        t = np.random.uniform(low=0, high=1.0, size=1)
        alpha0 = np.random.uniform(low=-0.7, high=0.3, size=1)
        alpha1 = np.random.uniform(low=0.1, high=0.2, size=1)
        alpha = alpha0 + t * alpha1
        if alpha < -0.9 or alpha > 0.1:
            break
        dist = Schechter(ellStar, alpha0, alpha1)

        v1 = dist.lnpdf_grad_ell(ell, t)

        def f_ell(ell):
            dist2 = Schechter(ellStar, alpha0, alpha1)
            return dist2.lnpdf(ell, t)
        v2 = derivative(f_ell, ell, dx=0.01*ell)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_t(ell, t)

        def f_t(t):
            dist2 = Schechter(ellStar, alpha0, alpha1)
            return dist2.lnpdf(ell, t)
        v2 = derivative(f_t, t, dx=0.01*t)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_alpha0(ell, t)

        def f_alpha0(alpha0):
            dist2 = Schechter(ellStar, alpha0, alpha1)
            return dist2.lnpdf(ell, t)
        v2 = derivative(f_alpha0, alpha0, dx=0.01*alpha0)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_alpha1(ell, t)

        def f_alpha1(alpha1):
            dist2 = Schechter(ellStar, alpha0, alpha1)
            return dist2.lnpdf(ell, t)
        v2 = derivative(f_alpha1, alpha1, dx=0.01*alpha1)
        assert abs(v1/v2-1) < 0.01


def test_kumaraswamy_derivatives():
    """
    Numerically test derivatives of Kumaraswamy distribution
    one by one for a few random parameters and values
    """
    for i in range(NREPEAT):
        t = np.random.uniform(low=0.1, high=0.9, size=1)
        alpha0 = np.random.uniform(low=0.2, high=10.0, size=1)
        alpha1 = np.random.uniform(low=0.2, high=10.0, size=1)
        dist = Kumaraswamy(alpha0, alpha1)
        print t, alpha0, alpha1
        v1 = dist.lnpdf_grad_t(t)

        def f_t(t, alpha0, alpha1):
            dist2 = Kumaraswamy(alpha0, alpha1)
            return dist2.lnpdf(t)
        v2 = derivative(f_t, t, dx=0.01*t, args=(alpha0, alpha1), order=5)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_alpha0(t)

        def f_alpha0(alpha0):
            dist2 = Kumaraswamy(alpha0, alpha1)
            return dist2.lnpdf(t)
        v2 = derivative(f_alpha0, alpha0, dx=0.01*alpha0)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_alpha1(t)

        def f_alpha1(alpha1):
            dist2 = Kumaraswamy(alpha0, alpha1)
            return dist2.lnpdf(t)
        v2 = derivative(f_alpha1, alpha1, dx=0.01*alpha1)
        assert abs(v1/v2-1) < 0.01


def test_rayleigh_derivatives():
    """
    Numerically test derivatives of Rayleigh distribution
    one by one for a few random parameters and values
    """
    for i in range(NREPEAT):
        z = np.random.uniform(low=0., high=3.0, size=1)
        t = np.random.uniform(low=0, high=1.0, size=1)
        alpha0 = np.random.uniform(low=0.2, high=2.0, size=1)
        alpha1 = np.random.uniform(low=0.2, high=2.0, size=1)
        alpha = alpha0 + t * alpha1
        dist = Rayleigh(alpha0, alpha1)

        v1 = dist.lnpdf_grad_z(z, t)

        def f_z(z):
            dist2 = Rayleigh(alpha0, alpha1)
            return dist2.lnpdf(z, t)
        v2 = derivative(f_z, z, dx=0.01*z)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_t(z, t)

        def f_t(t):
            dist2 = Rayleigh(alpha0, alpha1)
            return dist2.lnpdf(z, t)
        v2 = derivative(f_t, t, dx=0.01*t)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_alpha0(z, t)

        def f_alpha0(alpha0):
            dist2 = Rayleigh(alpha0, alpha1)
            return dist2.lnpdf(z, t)
        v2 = derivative(f_alpha0, alpha0, dx=0.01*alpha0)
        assert abs(v1/v2-1) < 0.01

        v1 = dist.lnpdf_grad_alpha1(z, t)

        def f_alpha1(alpha1):
            dist2 = Rayleigh(alpha0, alpha1)
            return dist2.lnpdf(z, t)
        v2 = derivative(f_alpha1, alpha1, dx=0.01*alpha1)
        assert abs(v1/v2-1) < 0.01
