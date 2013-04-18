<!DOCTYPE html>
<html>
    <head>
        <title>SQLite Queries</title>
    </head>
    <body>
        <h1>Enter a SQLite query:</h1>
        <form method="POST">
            <textarea name="query" cols="50" rows="10"></textarea>
            <input type="submit" value="Go" />
        </form>
        %if isinstance(result, list):
            %if len(result) > 0:
                <table border="1">
                <tr>
                    %for col in result[0].keys():
                        <th>{{ col }}</th>
                    %end
                </tr>
                %for row in result:
                    <tr>
                        %for col in row.keys():
                            <td>{{ row[col] }}</td>
                        %end
                    </tr>
                %end
                </table>
            %else:
                <p>
                    No rows returned.
                </p>
            %end
        %else:
            %if result:
                <p>
                    {{ result }}
                </p>
            %end
        %end
    </body>
</html>
