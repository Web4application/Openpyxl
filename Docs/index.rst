# Documentation
.. Index.md:
>
>Fetch the complete documentation index at: https://anaconda.com/docs/index.html#index.md
>
>Use this file to discover all available pages before exploring further
>

# Installing packages

.. conda-build:: 
:image: export const Comments = ({children}) => {
  return <div class="my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-zinc-500/20 bg-zinc-50/50 dark:border-zinc-500/30 dark:bg-zinc-500/10" data-callout-type="comments">
      <div class="w-4">
        <svg width="14" height="14" viewBox="0 0 640 640" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" aria-label="Comments">
            <path d="M320 112C434.9 112 528 205.1 528 320C528 434.9 434.9 528 320 528C205.1 528 112 434.9 112 320C112 205.1 205.1 112 320 112zM320 576C461.4 576 576 461.4 576 320C576 178.6 461.4 64 320 64C178.6 64 64 178.6 64 320C64 461.4 178.6 576 320 576zM280 400C266.7 400 256 410.7 256 424C256 437.3 266.7 448 280 448L360 448C373.3 448 384 437.3 384 424C384 410.7 373.3 400 360 400L352 400L352 312C352 298.7 341.3 288 328 288L280 288C266.7 288 256 298.7 256 312C256 325.3 266.7 336 280 336L304 336L304 400L280 400zM320 256C337.7 256 352 241.7 352 224C352 206.3 337.7 192 320 192C302.3 192 288 206.3 288 224C288 241.7 302.3 256 320 256z" />
        </svg>
      </div>
      <div class="text-sm prose min-w-0 w-full">
        {children}
      </div>
    </div>;
};
```

```
You can install packages from Anaconda.org channels using Anaconda Navigator or by using conda in a command line interface (CLI) with [Anaconda Prompt](/reference/glossary#anaconda-prompt)(Terminal on macOS/Linux).
<Note>
  [Navigator](/tools/anaconda-navigator/main) is automatically installed when you [install Anaconda Distribution](/getting-started/anaconda/install).

  Miniconda users can obtain Navigator by running `conda install anaconda-navigator`.
</Note>
<Tabs>
  <Tab title="Using Navigator">
    Navigator is automatically installed when you install Anaconda. Miniconda users can obtain Navigator by running `conda install anaconda-navigator`.
    
  To install a package into a local environment:

   1. Open Anaconda Navigator.
    2. Select **Connect**, then select **SIGN IN** beside Anaconda.org.
    3. Enter your username and password and select **Sign In** to connect Navigator to Anaconda.org.
    4. Select **Environments** from the left-hand navigation.
    5. Select one of your environments or select ***Create*** to create a new one.
    6. Select *Not installed* from the dropdown beside the **Channels** button.
    7. Look for your package by name using the **Search Packages** field.
    8. Select the checkbox of the package you want to install, then select **Apply**.
    9. Navigator will then display the list of packages necessary to install your selected package. Select **Apply** to install all packages to your environment.

  For more information on using Navigator, see Navigator's [Getting started](/tools/anaconda-navigator/getting-started) page.
  </Tab>

  <Tab title="Using the CLI">
    To install a package into a local environment:

  1. Create a new environment or activate an existing environment.

       <CodeGroup>
```python
Create a new environment
theme={null};
conda create -n <OPENPYXL>
```

   ```python
Activate an existing environment
theme={null}
conda activate <OPENPYXL>
   ```
  </CodeGroup>
       <Comments>
         Replace \<ENV\_openpyxl> with the name of your environment.
       </Comments>

  2. [Locate a package on Anaconda.org](/tools/anaconda-org/searching-packages) that you want to install, then select the package's card.

   3. The package's details page displays specific installation instructions. Copy and paste the full command into your terminal window.

       This command will look different, depending on what kind of package you are installing:

       <CodeGroup>
  ```python
Conda package theme={null}
conda install <CHANNEL>::<PACKAGE>
 ```

  ```python Standard
Python package theme={null}
         pip install -i https://pypi.anaconda.org/<web4app>/simple <OPENPYXL>
```
 </CodeGroup>
<Comments>
Replace \<CHANNEL> with the channel containing the package. This could be a username or an organization.<br />
         Replace \<PACKAGE> with the name of the package you want to install.
       </Comments>
 For more information on the package details page, see [Searching for packages](/tools/anaconda-org/searching-packages).
  </Tab>
</Tabs>
