# OpenFaas Functions

Read my blog on [OpenFaas Functions](https://dev.to/yankee/deploy-your-serverless-python-function-locally-with-openfaas-in-kubernetes-18jf)

## 1. [pydict](https://github.com/yankeexe/openfaas-functions/tree/master/pydict)
Returns meaning of words provided.

<details><summary><b>Installation Instructions</b></summary>

**Build, Push, and Deploy the function** 
```bash
faas-cli build -f functions.yml --filter pydict

faas-cli push -f functions.yml --filter pydict

faas-cli deploy -f functions.yml --filter pydict
```

**Invoke the function:**

```bash
echo "brevity" | faas-cli invoke pydict
```

</details>

## 2. [ytdl](https://github.com/yankeexe/openfaas-functions/tree/master/ytdl)
Download mp3 from provided URL
<details><summary><b>Installation Instructions</b></summary>

**Build, Push, and Deploy the function** 
```bash
faas-cli build -f functions.yml --filter ytdl -b ADDITIONAL_PACKAGE=ffmpeg

faas-cli push -f functions.yml --filter ytdl

faas-cli deploy -f functions.yml --filter ytdl
```

**Invoke the function:**

```bash
echo "<url>" | faas-cli invoke ytdl > <filename.mp3>
```

</details>

