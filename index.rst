> ## Documentation Index
> Fetch the complete documentation index at: https://anaconda.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Anaconda Code

export const TroubleshootSolution = ({children}) => <>
    <hr className="my-3 w-full" />
    <details className="mt-3">
      <summary className="cursor-pointer font-semibold text-base mb-1">
        Solution
      </summary>
      <div className="mt-2 ml-4" data-component-part="step-content">
        {children}
      </div>
    </details>
  </>;

export const TroubleshootCause = ({children}) => <details className="mt-3 mb-2">
    <summary className="cursor-pointer font-semibold text-base mb-1">
      Cause
    </summary>
    <div className="mt-2 ml-4" data-component-part="step-content">
      {children}
    </div>
  </details>;

export const TroubleshootTitle = ({children}) => <>
    <p className="m-0 font-semibold text-xl leading-tight mb-2" role="heading" aria-level={3}>
      {children}
    </p>
    <hr className="my-3 w-full" />
  </>;

export const Troubleshoot = ({children}) => <div className="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border troubleshoot-admonition dark:troubleshoot-admonition" data-callout-type="troubleshoot">
    <div className="mt-0.5 w-4">
      <svg width="14" height="14" viewBox="0 0 640 640" fill="currentColor" className="w-4 h-4" aria-label="Troubleshoot">
        <path d="M541.4 162.6C549 155 561.7 156.9 565.5 166.9C572.3 184.6 576 203.9 576 224C576 312.4 504.4 384 416 384C398.5 384 381.6 381.2 365.8 376L178.9 562.9C150.8 591 105.2 591 77.1 562.9C49 534.8 49 489.2 77.1 461.1L264 274.2C258.8 258.4 256 241.6 256 224C256 135.6 327.6 64 416 64C436.1 64 455.4 67.7 473.1 74.5C483.1 78.3 484.9 91 477.4 98.6L388.7 187.3C385.7 190.3 384 194.4 384 198.6L384 240C384 248.8 391.2 256 400 256L441.4 256C445.6 256 449.7 254.3 452.7 251.3L541.4 162.6z" />
      </svg>
    </div>
    <div className="prose min-w-0 w-full">{children}</div>
  </div>;

export const ExcelRefIcon = () => {
  return <span className="inline_icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 60.51 26.3">
            <path fill="currentColor" d="M0,26.3V0H8.89c2.05,0,3.74,.35,5.06,1.05,1.32,.7,2.29,1.65,2.93,2.87,.63,1.22,.95,2.6,.95,4.15s-.32,2.92-.95,4.12c-.63,1.2-1.61,2.14-2.92,2.82-1.31,.68-2.98,1.02-5.02,1.02H1.75v-2.88h7.09c1.4,0,2.54-.21,3.4-.62s1.49-1,1.88-1.75,.58-1.66,.58-2.72-.2-1.97-.59-2.76c-.39-.79-1.02-1.4-1.89-1.83-.87-.43-2.01-.65-3.43-.65H3.19V26.3H0ZM12.38,14.49l6.47,11.82h-3.7l-6.37-11.82h3.6Z" /><path fill="currentColor" d="M23.12,26.3V0h15.87V2.83h-12.69V11.71h11.87v2.83h-11.87v8.94h12.89v2.83H23.12Z" /><path fill="currentColor" d="M44.74,26.3V0h15.77V2.83h-12.59V11.71h11.4v2.83h-11.4v11.76h-3.19Z" />
            </svg>
        </span>;
};

export const ExcelCellAddressIcon = () => {
  return <span className="inline_icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 37.91 29.1">
            <path fill="currentColor" d="M3.69,29.1H0L10.68,0h3.64l10.68,29.1h-3.69L12.62,4.6h-.23L3.69,29.1Zm1.36-11.37h14.89v3.13H5.06v-3.13Z" /><path fill="currentColor" d="M37.91,0V29.1h-3.52V3.69h-.17l-7.1,4.72v-3.58L34.38,0h3.52Z" />
            </svg>
        </span>;
};

<Note>
  This feature is currently in beta.
</Note>

Anaconda Code empowers you to write Python or R code and run it locally, directly within Excel. This gives you flexibility and control over the environment in your workbook, allowing you to add and remove <Tooltip tip="Software files and information about the software, such as its name, version, and description, bundled into a file that can be installed and managed by a package manager.">packages</Tooltip> as needed, all while keeping code and data securely within your workbook. Anaconda Code operates independently of Microsoft's Python in Excel feature.

## Initializing Anaconda Code

<Note>
  Anaconda Code is included in the [Anaconda Toolbox installation](/tools/excel/install).
</Note>

When you first launch Anaconda Code, you'll be asked to [sign in to your Anaconda account](https://auth.anaconda.cloud/ui/login/).

If you haven't created an Anaconda Code cell yet, you'll be asked to create one.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=3cde08bfec3755a6dae5d16a6974e404" alt="" style={{ width: "400px" }} data-og-width="832" width="832" data-og-height="1580" height="1580" data-path="images/excel_code_get_started.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=280&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=c90762e302071acaf51c888d70bc8582 280w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=560&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=7b4100827e665c89abe90a656634b2ee 560w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=840&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=c78e4c5fbb86ef0a6b20bfb0ad13fcd4 840w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=1100&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=5d7c3ec52c5f8af8b1d806f04ad3ba0f 1100w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=1650&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=83fa3152537c73d47503c3021078e46a 1650w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=2500&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=a0fbe8f38a065cba09ad7e813c81bcd1 2500w" />
</Frame>

To get started, choose the [language](#running-code) for your new Anaconda Code cell, set the [default link mode](#cell-linking), select the [default output mode](#cell-output), and then click <Icon icon="plus" iconType="regular" /> **Create Code Cell**.

Once you've selected a location for your new Anaconda Code cell, use the editor to start [writing and running code](#running-code).

## Understanding Anaconda Code

Let's take a look at the different elements within Anaconda Code using the <Icon icon="house-chimney" iconType="light" /> **Home** tab for reference:

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=032b6d2170677e6aa91ed7fae804c461" alt="" style={{ width: "400px" }} data-og-width="1026" width="1026" data-og-height="1308" height="1308" data-path="images/code_anatomy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5127e95c25fb99555d35d1154fc40732 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e5afd4320d05b465ee4843e8487e16d2 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=85c39032e894d956c625231b0c68af64 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9b5e9faa437614dc5fbd202534ffbdd0 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0b718c96c73f621232bd8191937ad0ad 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=b3e67c21c827510dec011e1098ff2955 2500w" />
</Frame>

<Steps>
  <Step title="Home" icon={<Icon icon="house-chimney" iconType="light" />}>
    [Create and run Python or R code](#running-code)
  </Step>

  <Step title="Imports and Definitions" icon={<Icon icon="file-import" iconType="light" />}>
    [Customize the code](#customizing-code-initialization) that affects all code
    in your workbook and view script logs
  </Step>

  <Step title="Environment" icon={<Icon icon="laptop-code" iconType="light" />}>
    [Manage the packages and Pyodide or WebR version](#managing-the-environment) for your
    coding environment
  </Step>

  <Step title="Settings" icon={<Icon icon="gear" iconType="light" />}>
    Modify the [default settings for running code](#modifying-workbook-settings)
  </Step>

  <Step title="Account" icon={<Icon icon="user" iconType="light" />}>
    View profile, subscriptions, sign out, and app details
  </Step>

  <Step title="Help" icon={<Icon icon="circle-question" iconType="light" />}>
    Access bug reporting, documentation, community forums, and privacy policy links
  </Step>

  <Step title="Active Code Cell Reference" icon={<ExcelCellAddressIcon />}>
    The active code cell where your [code will run](#running-code)
  </Step>

  <Step title="Linking" icon={<Icon icon="link-simple-slash" iconType="light" />}>
    Toggle [cell linking](#cell-linking) between <Icon icon="link-simple-slash" iconType="light" /> **isolated** and <Icon icon="link-simple" iconType="light" /> **linked** modes
  </Step>

  <Step title="Cell Output" icon={<Icon icon="hashtag" iconType="light" />}>
    Choose whether to output [cell values](#cell-output) as an <Icon icon="hashtag" iconType="light" /> **Excel value** or an <Icon icon="code" iconType="light" /> **Anaconda Code object**
  </Step>

  <Step title="Language" icon={<Icon icon="python" iconType="brands" />}>
    Select <Icon icon="python" iconType="brands" /> **Python** or <Icon icon="r-project" iconType="brands" /> **R** for the code cell
  </Step>

  <Step title="Delete" icon={<Icon icon="trash-can" iconType="light" />}>
    Delete the code cell
  </Step>

  <Step title="Copy" icon={<Icon icon="copy" iconType="light" />}>
    Copy the contents of the code editor
  </Step>

  <Step title="REF" icon={<ExcelRefIcon />}>
    Create a [reference](#using-the-ref-function) to data in the worksheet.
  </Step>

  <Step title="Run" icon={<Icon icon="play" iconType="light" />}>
    Run the code in the active code cell
  </Step>
</Steps>

## Running code

Create an Anaconda Code cell that can run Python or R code using the following steps:

1. From <Icon icon="house-chimney" iconType="light" /> **Home**, click <Icon icon="plus" iconType="regular" aria-label="plus icon" />, then select a cell where you want to insert your code.

   <Tip>
     If you're already in the code editor, select <Icon icon="chevron-down" iconType="light" /> **more** next to the active code cell reference, then <Icon icon="plus" iconType="regular" /> **Add New** to create a new code cell.
   </Tip>

   <Note>
     Subsequent code cells will be in the same language as the previously created one. To change the language, first create a new code cell, then change the code cell's language selection in the code editor.
   </Note>

2. Set the [cell linking and output options](#modifying-workbook-settings).

3. Select Python or R as the code language for the cell.

   <Note>
     If you change the language for the cell to a language you haven't yet used, you might need to click **Load Environment** to load the new language's environment for the first time.
   </Note>

4. Enter your code in the code editor.

5. *(Optional)* If you want to reference a range of data from your spreadsheet or an [Anaconda Code object](/tools/excel/toolbox/data#downloading-data) in your code, click **REF**, then select the range of cells or Anaconda Code cell.

   <Accordion title="Using the REF function">
     When you use **REF** to select data cells or Anaconda Code cells, Anaconda Code creates a `REF` function in your code that returns a list of lists. The [Imports and Definitions](#customizing-code-initialization) tab includes the following pre-defined functions to help convert the returned list of lists to different data structures.

     <Tabs>
       <Tab title="Python">
         | Function                      | Use case                                                                                 | Notes                                                   |
         | :---------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------ |
         | `to_df(REF(<CELL_RANGE>))`    | Create a [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) | `to_df` assumes your data has headers                   |
         | `to_array(REF(<CELL_RANGE>))` | Create a [NumPy](https://numpy.org/) array                                               | `to_array` assumes all data is of the same type         |
         | `to_list(REF(<CELL_RANGE>))`  | Create a 1D list                                                                         | `to_list` handles wide (1 x *n*) or tall (*n* x 1) data |

         You can change the behavior of `to_df()`, `to_array()`, and `to_list()` from the [Imports and Definitions](#customizing-code-initialization) tab.
       </Tab>

       <Tab title="R">
         | Function             | Use case                                                                   | Notes                                                                                     |
         | :------------------- | :------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
         | `to_dataframe()`     | Convert to data.frame or tidyverse [tibble](https://tibble.tidyverse.org/) | Converts a list of lists to tabular format, using first row as column names, if available |
         | `to_matrix()`        | Convert to matrix                                                          | Converts a list of lists to a matrix structure                                            |
         | `to_colwise_list()`  | Convert to column-wise list of vectors                                     | Transforms row-wise data (list of lists) into column-wise format                          |
         | `is_list_of_lists()` | Check data structure                                                       | Helper function that verifies if input is properly structured as a list of lists          |

         You can change the behavior of `to_dataframe`, `to_matrix()`, `to_colwise_list()`,  and `is_list_of_lists()` from the [Imports and Definitions](#customizing-code-initialization) tab.
       </Tab>
     </Tabs>
   </Accordion>

6. Click **Run**. The cell will display the return value of the last evaluated expression. Your changes are automatically saved whenever you re-run the code.

   <Note>
     If you write code that doesn't have a return value (for example, you define a function but don't call the function) and click **Run**, the cell will display `</>NoneType`.
   </Note>

## Editing code

Do not edit your code in the cell itself; instead, modify and re-run your code directly in Anaconda Code.

<Note>
  An Anaconda.com account is required for users to edit shared code.
</Note>

1. From the <Icon icon="house-chimney" iconType="light" /> **Home** page, click <Icon icon="chevron-down" iconType="light" /> **more** on the code you want to edit.
2. Click <Icon icon="pen" iconType="light" /> **Edit in full view** to open the edit view.
3. Adjust your code, then click **Run**.

## Managing the environment

Anaconda Code hosts a single, self-contained environment, which manages the back-end software packages that enable you to run Python or R code within your Excel workbook. You can manage software packages within this environment to extend your code's processing, visualization, and analytical capabilities, and even select the version of [Pyodide](https://pyodide.org/en/stable/) (the WASM engine used by PyScript) or [WebR](https://docs.r-wasm.org/webr/latest/) (the WASM engine used by WebR) that you want to run.

<Warning>
  You can make changes to your environment at any time; however, like with all software projects, altering the environment changes the way the underlying code is interpreted and can cause unintended complications.
</Warning>

### Choosing a Pyodide or WebR version

The latest version of Pyodide or WebR is used by default for all new spreadsheets. For existing spreadsheets, the Pyodide or WebR versions and packages necessary for your code are pinned to the environment.

You can switch versions using the following steps:

1. From the <Icon icon="laptop-code" iconType="light" /> **Environment** tab, click <Icon icon="pen" iconType="light" /> **Edit**.
2. Select the Pyodide or WebR version.
3. Click **Save Changes**.

<Warning>
  A warning will appear if changing the version might result in conflicts with the installed packages. Click **Confirm Update** to proceed or **Cancel** to revert to the previously selected version.
</Warning>

### Managing software packages

1. From the  <Icon icon="laptop-code" iconType="light" /> **Environment** tab, click <Icon icon="pen" iconType="light" /> **Edit**.
2. To add new packages, click <Icon icon="plus" iconType="regular" /> **Add**.
3. *(Optional for Python)* Click the <Icon icon="caret-down" iconType="solid" /> down arrow to add from either PyPI, the PyScript app, or a direct download link to a Python wheel (`.whl`).
4. Search for the package name, then click <Icon icon="plus" iconType="regular" /> **Add** beside the package you want to add.
5. Once you've added all the packages you want to include, click **Add Packages**.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=348fb9b6773a0d83bb96865b4ffd32e2" alt="" style={{ width: "400px" }} data-og-width="1026" width="1026" data-og-height="1580" height="1580" data-path="images/code_add_package.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=7d789112ed04664f7636b4b321d34755 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=fad0116a58ba6f560634eafdefd884a7 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=13eaddaf0de0fe56e5e52afa35fc5cd9 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e9f680eb0753e65901164ee1c51d8e4a 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=65f287b64bfbca38533dfa17cd05269b 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=f25cdcabd0baafec40f544b70665d701 2500w" />
</Frame>

<Note>
  Packages that contain compiled code might not be compatible with the PyScript or R WASM engine. For more information, visit [PyScript.net](https://pyscript.net/) or [r-wasm.org](https://docs.r-wasm.org/webr/latest/packages.html).
</Note>

To remove a package, click <Icon icon="pen" iconType="light" /> **Edit**, then click <Icon icon="trash-can" iconType="regular" /> **Delete** beside the package you want to remove.

## Customizing code initialization

You can think of Anaconda Code's **Imports and Definitions** as an initialization file for your code or like the first cell in a Jupyter Notebook. All code in this section is available to all cells, whether they are [run isolated or linked](#cell-linking).

<AccordionGroup>
  <Accordion title="Imports">
    To customize your code's imports:

    1. On the <Icon icon="file-import" iconType="light" /> **Imports and Definitions** tab, establish the connections to the packages you need to run your code by adding your import statements beneath the `# Add imports` comment.

       <Note>
         You can only `import` from the packages included in the standard Python or Web R installation and those listed in the **Environment** tab.
       </Note>

    2. Click **Apply**.
  </Accordion>

  <Accordion title="Definitions">
    To customize your code's definitions:

    1. From the <Icon icon="file-import" iconType="light" /> **Imports and Definitions** tab, enter any classes or functions you'd like to define beneath the `# Define` comment.

       <Note>
         Anaconda Code comes with pre-defined functions for both Python and R. See [Using the REF function](#using-the-ref-function) to learn more about using these functions.
       </Note>

    2. Click **Apply**.

    You can now call your definitions in the Anaconda Code editor. To call Python functions directly from a spreadsheet cell, follow the steps in [Creating user-defined functions](#creating-user-defined-functions).
  </Accordion>
</AccordionGroup>

### Creating user-defined functions

User-defined functions (UDFs) allow you to write Python or R functions and call them directly from a spreadsheet cell.

<AccordionGroup>
  <Accordion title="UDFs in Python">
    **Creating and calling a UDF**

    1. From the **Imports and Definitions** tab, decorate a function with `@UDF`, as shown in the following example:

       ```py Python UDF Example theme={null}
       @UDF
       def my_custom_function(x, y):
           return x ** y
       ```

    2. Click **Apply**.

    3. In an open cell, enter `=ANACONDA`. If you added the example above to your definitions list, the option to call `ANACONDA.MY_CUSTOM_FUNCTION`
       appears in the dropdown.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5572b0cd0c91b1ec16f37833f8da0072" alt="" data-og-width="1704" width="1704" data-og-height="1428" height="1428" data-path="images/create_udf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=247d5352f34acb749de8c9f02c18240f 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=88f9b79bded922be591f1f8c0ab8ba03 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=066833229713b5d3a64cc6e8037c456c 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=fa27c4109d98adf81c92b28f554e5f86 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9b6d9cd3ee1b3d56255efe1bddc9a93e 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=74d66126646824dc6fc053a42fb8d0fe 2500w" />
       </Frame>

    4. Arrow down to `ANACONDA.MY_CUSTOM_FUNCTION`, press Tab, and then complete the function.

    5. Use Ctrl+Enter (Windows)/Ctrl+Return (macOS) to run the code.

    <Tip>
      If you'd prefer the UDF uses a name other than the function name, use the `name` argument to provide a unique name. Set `nested` to False to remove `ANACONDA.` from the name.

      ```py Renaming Python UDF Example theme={null}
      @UDF(name="MYBANK.PORTFOLIO_ANALYSIS", nested=False)
      def my_custom_function(x, y):
          return x ** y

      ```

      <Frame>
        <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=373fe4433136ca79c235ad8ca82c2f75" alt="" data-og-width="1698" width="1698" data-og-height="1428" height="1428" data-path="images/create_udf_custom_name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0c732829a891824eef2bcd3f1765180d 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=851c16b280782e58675068d8a9f342da 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=7d19999c27fc6440d58bebe0beb2e9f6 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=b69b4fbbc3433f8bc6d85748128a4d7d 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1fcda28ebc077cb9b82a3cc61e397369 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=701b6b1bb35d0ed9a4458461534c76e4 2500w" />
      </Frame>
    </Tip>

    **Using range arguments**

    Specifying a `UDF.Range` argument tells Excel that the input of the function is a 2D range. Without specifying this, Excel will show a `#CALC! Unliftable Array` error if a 2D range is passed into the UDF. Parameters specified as `UDF.Range` will always be passed as a 2D array to the function, even if a single cell is passed in.

    Example usage of `UDF.Range`:

    ```py Python Range Example theme={null}
    @UDF
    def square_me(data: UDF.Range) -> UDF.Range:
        return [[val ** 2 for val in row] for row in data]

    ```

    You can also add type hints for ranges. For example,`UDF.Range[str]`.
  </Accordion>

  <Accordion title="UDFs in R">
    **Creating and calling a UDF**

    1. From the **Imports and Definitions** tab, register the UDF with `UDF.register()` and pass the function as an argument, as shown in the following example:

       <Note>
         The UDF must be registered after the function is defined.
       </Note>

       ```r R UDF Example theme={null}
       my_custom_r_function <- function(x, y) {
           x ^ y
       }
       UDF.register(my_custom_r_function)
       ```

    2. Click **Save and Apply**.

    3. In an open cell, enter `=ANACONDA`. If you added the example above to your definitions list, the option to call `ANACONDA.MY_CUSTOM_R_FUNCTION`
       appears in the dropdown.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=010bdb18a5ff8d5bc2bc38940eb0e120" alt="" data-og-width="1734" width="1734" data-og-height="1716" height="1716" data-path="images/create_udf_r.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1239e88fdc6a9cfa062897f742b8bc1c 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=ffb973876271c5c2f50b60b61b7bb4c2 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=332b09f3ae0ff6e2942ea545ef03ca2a 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0348520653693a4a1ca82e8f6b4ebc29 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=74a2709a286a9b5afadd15175432749d 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=fa64c6ee67a4c6f4e081990aa68b4ad1 2500w" />
       </Frame>

    4. Arrow down to `ANACONDA.MY_CUSTOM_R_FUNCTION`, press Tab, and then complete the function call.

    5. Use Ctrl+Enter (Windows)/Ctrl+Return (macOS) to run the code.

    <Tip>
      If you'd prefer the UDF uses a name other than the function name, register the function with the UDF, then use the `name` argument to provide a unique name and set `nested` to False to remove `ANACONDA.` from the name.

      ```r Renaming R UDF Example theme={null}
      my_custom_r_function <- function(x, y) {
          x ^ y
      }
      UDF.register(my_custom_r_function, name="MYBANK.PORTFOLIO_ANALYSIS", nested=FALSE)
      ```

      <Frame>
        <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=bbe57a6e5a269a3291421899cbbb5654" alt="" data-og-width="1694" width="1694" data-og-height="1712" height="1712" data-path="images/create_udf_r_custom_name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1c8cb2c1c1ad3a50d61d5bbddff9e482 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=69b44583db7858fb51aef174c9687e2d 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e64878144f327129b4cfb363cf60f712 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5a7203d44ecffc992850bdce56bd0fb0 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=13195fc72350cd26e725307f3a8e8ff7 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=2848fabfdc2a327fbe4a6262354cc776 2500w" />
      </Frame>
    </Tip>

    **Using range arguments**

    Setting the `range_args` parameter tells Excel that the input of the function is a 2D range.  Without specifying this, Excel will show a `#CALC! Unliftable Array` error if a 2D range is passed into the UDF. Parameters specified as `range_args` will always be passed as a 2D array to the function, even if a single cell is passed in.

    Example usage of `range_args`:

    ```r R Range Example theme={null}
    my_custom_r_function <- function(data) {
        sum(data)
    }
    UDF.register(my_custom_r_function, range_args=c("data"))
    ```

    **Adding function documentation**

    To add documentation to your function, use the `doc` parameter:

    ```r R Documentation Example theme={null}
    my_custom_r_function <- function(x, y) {
        x ^ y
    }
    UDF.register(my_custom_r_function, doc="Computes x raised to the power of y.")
    ```
  </Accordion>
</AccordionGroup>

## Modifying workbook settings

While you can adjust the settings for running code in your workbook on a case-by-case basis when creating and editing code, you can also assign default settings from the **Settings** tab.

### Cell linking

<AccordionGroup>
  <Accordion title="Run Isolated">
    When a code cell is run in <Icon icon="link-simple-slash" iconType="light" /> **isolated** mode, its code runs independently of other cells. Variables defined within an isolated code cell can't be referenced by other code cells, and variables in other code cells likewise can't be referenced by the isolated code cell.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e28a4ac7b0c21c11b11f4947f303d02c" alt="Two code cells in isolated mode where the second cell cannot access variables from the first" data-og-width="1684" width="1684" data-og-height="948" height="948" data-path="images/cell_isolated_mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=cc926655d310e577b8d716461bab68a6 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=7d8061a23efbb3d233fde9e387c98420 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=bf8d89742812a7cbca0caeca37f2562b 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=2b3785789f9b826b69fe4b6e32e3a76a 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=b552bbb1e33607ce2b90415a01e889ee 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=75b04f2cbcbd411a62405774e632172d 2500w" />
    </Frame>

    In the above image, the `output_of_B2` variable is defined in cell B2 and assigned the string `"I'm the B2 cell!"`. When this code is run in the B2 code cell, the B2 cell displays `"I'm the B2 cell!"`. However, since both cells are running in isolated mode, when `output_of_B2` is referenced in the B4 code cell, the B4 cell displays a `#VALUE!` error because B4 cannot access the variable in B2.

    **Using the `REF` function**

    You can bypass isolation rules as needed using the `REF` function to create a reference from one isolated code cell to another.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=0a6287dd90c0c73498e23d6557133461" alt="A code cell using the REF function to reference another cell's output" data-og-width="1704" width="1704" data-og-height="962" height="962" data-path="images/isolated_ref_cell.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=280&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=b56a71f44090f7a49c6cd2fa07fed96b 280w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=560&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=966d9ab29e616226cd6c3eeca069b4d9 560w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=840&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=78a913f30c04c90f1e3c5f2653d60824 840w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=1100&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=68fed1efc9937f1bbe78c4c4dd9b25c6 1100w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=1650&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=73d17eaa5428cff9c8aa85b61a8f937b 1650w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=2500&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=21f7f82c541d536e9dd555243fd1ed02 2500w" />
    </Frame>

    In the above image, the B4 cell now includes a reference to the B2 cell, `REF("B2")`. When the B4 code cell is run, it returns the value of B2, `"I'm the B2 cell!"`. Changes to the B4 cell don't cause the B2 cell to recalculate, but changes to the B2 cell will cause the B4 cell to recalculate. Code cells can include multiple `REF` function references, and changes to any referenced cells (in this example, B2) will cause the referencing cells to recalculate (in this example, B4).

    **Working with code objects**

    If you reference a cell that's set to output a code object, the `REF` function will return an instance of that object in the referencing cell.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=a88c0a285d085c14ab3c12afe5120cb8" alt="A code cell referencing another cell that outputs a list object" data-og-width="1718" width="1718" data-og-height="968" height="968" data-path="images/code_object_isolated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9701200f23ffc2a1393da4012ea21c45 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=33680dd70b91eb2c9cbe4fddbd252bf7 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e99f2aff1f205424347212780948291c 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=ad5325ba43d4a75b05fbe424db54083c 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=addd1a2ae6323b3829d2ced2df6235dc 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=4d31cd9b92a61ba53043b2ad2e460514 2500w" />
    </Frame>

    In the above image, the B2 code cell is set to output a code object (in this case, a list). Because the output of B2 is a <Tooltip tip="A non-scalar value is a data structure that contains multiple values, such as a list, dictionary, or tuple.">non-scalar value</Tooltip>, we see `</> list` in B2. In the B4 code cell, we define a variable called `output_of_B2` and assign a `REF` function that references cell B2. The output mode for the B4 code cell is set to "Excel Values", so the list spills across multiple cells in the spreadsheet.

    **Benefits of isolated mode**

    The benefit of using the isolated mode is that referenced cells are not recalculated when changes are made to referencing cells. For complex processes, this allows you to:

    * separate code that doesn't change frequently from code you modify often.
    * reduce unnecessary recalculations of computationally intensive operations.
    * create a more modular approach to your data analysis.
    * improve performance when working with larger datasets.
  </Accordion>

  <Accordion title="Run Linked">
    When a code cell is run in <Icon icon="link-simple" iconType="light" /> **linked** mode, variables defined within it can be accessed by any other code cell also running in linked mode. When any linked mode cell is recalculated, all linked mode cells are recalculated. Linked cells run left-to-right, top-to-bottom, and can access objects defined in previously linked cells.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e4be8b9c4344868b197fef9062b442b6" alt="" data-og-width="1698" width="1698" data-og-height="952" height="952" data-path="images/cell_linked_mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=3d8e440d25369edf953f0400a37991c8 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e52b875cdd5cabe82921e39e94cdb9bf 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=4c5f84e2322fb3ea57ef0a60e76c0053 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=be2fc5900b83edc477e12dd6c17c6c1b 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=785ebaa8887db14cc357ee7716cc60be 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=29443653e2dcf1186f59fbccf9a50790 2500w" />
    </Frame>

    In the above image, both the B2 and B4 cell are running in linked mode. The `output_of_B2` variable is defined in cell B2 and assigned the string `"I'm the B2 cell!"`. When this code is run in the B2 code cell, the B2 cell displays `"I'm the B2 cell!"`. The `output_of_B2` variable is then referenced in the B4 code cell, causing the B4 cell to also display `"I'm the B2 cell!"`.

    **Benefits of linked mode**

    Linked mode is useful when:

    * you want to create a continuous workflow across multiple cells.
    * you need to share variables and objects between different parts of your analysis.
    * your code follows a linear execution path.
  </Accordion>
</AccordionGroup>

### Cell output

| Output            | Description                                                                                                                                                                                        |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Excel Values      | When outputting a DataFrame, array, list, and so on, the values will "spill" to fill the required space. If the spill were to overwrite cells containing data, the cell displays a `#SPILL` error. |
| Local Code Object | For certain object types, you can view the contents in a "Card View" by clicking the cell. You can reference this cell and the returned object like you would any other object.                    |

## Troubleshooting

If you encounter an issue that is not listed here, you can obtain support for Anaconda through the [Anaconda community forums](https://forum.anaconda.com) or by [opening a support ticket](https://support.anaconda.com/hc/en-us/requests/new?ticket_form_id=360000993773).

<Troubleshoot>
  <TroubleshootTitle>
    ### Error installing functions in Excel
  </TroubleshootTitle>

  <TroubleshootCause>
    This error can occur when Excel loads the Anaconda Toolbox add-in and registers its custom functions. This error happens within Excel and cannot be resolved by the Anaconda Toolbox.
  </TroubleshootCause>

  <TroubleshootSolution>
    Close and reopen Excel. If the issue persists, uninstall the Anaconda Toolbox add-in, then reinstall.
  </TroubleshootSolution>
</Troubleshoot>
