<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">
<head>
    <title>PyOpenGL ${version} Function Reference</title>
</head>
<body>

<h1>PyOpenGL ${version}</h1>
<ul class="toc"><li py:for="package in ref.package_names()">
    <a href="#${package}">${package} Reference</a>
</li></ul>

<div py:for="(package,sections) in ref.packages()" class="reference">
    <h2 class="package-title"><a name="${package}"/>${package} Reference</h2>
    <table><tbody><tr ><th align="right">Function</th><th>Purpose</th></tr>
    <tr py:for="name,section in sections" valign="top">
        <th align="right" class="section-name">
            <a href="${ref.url(section)}">${name}</a>
        </th>
        <td class="purpose">${section.purpose}</td>
    </tr>
    </tbody></table>
</div>

</body>
</html>

