
## commands for training models and generating saved models (for analysing step)

Appendix:
> For p(z) = N (z; 0, diag(σ)), experiments were run with 
> a batch size of 64 and for 20 epochs. For p(z) = 􏰐d STUDENT-T(zd; ν), 
> experiments were run with a batch size of 256 and for 40 epochs"

### T-Student's with different degrees of freedom
```
# here batch size and nb epochs different; choose anyway 20, otherwise too much time
DF=2; python main.py --cuda-dev=4 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=5; python main.py --cuda-dev=4 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=9; python main.py --cuda-dev=2 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=12; python main.py --cuda-dev=2 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=9999; python main.py --cuda-dev=6 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF

```

### Isotropic gaussian or anistropic gaussian with learned or fixed PCA

```

BETA=1 python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=1 python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=1 python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=2; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=2; python main.py --cuda-dev=7 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=2; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=4; python main.py --cuda-dev=9 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=4; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=4; python main.py --cuda-dev=7 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=8; python main.py --cuda-dev=7 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=8; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=8; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=16; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=16; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=16; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance
```## commands for training models and generating saved models (for analysing step)
Appendix:

"For p(z) = N (z; 0, diag(σ)), experiments were run with 

a batch size of 64 and for 20 epochs. For p(z) = 􏰐d STUDENT-T(zd; ν), 

experiments were run with a batch size of 256 and for 40 epochs"

### T-Student's with different degrees of freedom
```
# here batch size and nb epochs different; choose anyway 20, otherwise too much time
DF=2; python main.py --cuda-dev=4 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=5; python main.py --cuda-dev=4 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=9; python main.py --cuda-dev=2 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=12; python main.py --cuda-dev=2 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF
DF=9999; python main.py --cuda-dev=6 --name dsprites_beta_1_pz_st_$DF --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 256 --latent-dim 10 --beta 1. --prior StudentT --df $DF

```

### Isotropic gaussian or anistropic gaussian with learned or fixed PCA

```

BETA=1 python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=1 python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=1 python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=2; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=2; python main.py --cuda-dev=7 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=2; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=4; python main.py --cuda-dev=9 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=4; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=4; python main.py --cuda-dev=7 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=8; python main.py --cuda-dev=7 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=8; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=8; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance

# --- done

BETA=16; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_iso --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance iso
BETA=16; python main.py --cuda-dev=8 --name dsprites_beta_$BETA\_pz_norm_pca --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca
BETA=16; python main.py --cuda-dev=6 --name dsprites_beta_$BETA\_pz_norm_pca_learn --model dsprites \
    --skip-test --epochs 20 --lr 1e-4 --batch-size 64 --latent-dim 10 --beta $BETA --prior-variance pca \
    --learn-prior-variance
```
