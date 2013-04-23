<!DOCTYPE html>
<html>
    <head>
        <title>Crazy Eddie's discount URL shortener</title>
    </head>
    <body>
        <h1>Enter an URL to shorten</h1>
        <p>(or a shortened URL to preview)</p>
        <form method="POST">
            <input type="text" name="input_url" size="50"
            %if defined('input_url'):
                value="{{ input_url }}"
            %end
            />
            <input type="submit" value="Go" />
        </form>
        %if defined('output_url'):
            <h2><a href="{{ output_url }}">{{ output_url }}</a></h2>
        %end
        %if popular:
            <h3>Popular Links</h3>
            <ul>
                %for link, hits in popular:
                    <li>{{! link }} ({{ int(hits) }} hits)</li>
                %end
            </ul>
        %end
    </body>
</html>
