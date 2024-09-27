#Usa una imagen base de .NET SDK
FROM mcr.microsoft.com/dotnet/sdk: 8.0 AS build
# Configura el directorio de trabajo
WORKDIR /app
# Copia el archivo .csproj y restaura dependencias 
COPY *.csproj ./
RUN dotnet restore
# Copia el código fuente y compilalo 
COPY . ./
RUN dotnet publish -c Release -o /out
# Usa una imagen de runtime más ligera
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime 
WORKDIR /app
COPY --from-build /out
ENTRYPOINT ["dotnet", "VoteWorker.dll"]