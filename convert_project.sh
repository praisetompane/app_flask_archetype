#!/bin/zsh

# rename app_flask_archetype to a desired target project name
# input:
#   target_app_name: str
#
target_app_name=$1
current_project_name=app_flask_archetype

function process_file() {
    file=$1
    sed -i "" -e "s/$current_project_name/$target_app_name/g" $file
}

if [ -z "$target_app_name" ]; then
    echo "target_app_name cannot be empty. Please supply package name."
else
    echo "Renaming Project to $target_app_name"

    echo "Processing Files"
        for file in **/*.*; do
        if [[ $file != *".png"* ]]; then
            echo "Processing $file\n"
            process_file $file
        fi
        done
    echo "Done Processing Files"

    echo "Processing devcontainer folder"
        for file in .devcontainer/*.*; do
            echo "Processing $file\n"
            process_file $file
        done
    echo "Done Processing devcontainers Folder"

    echo "Processing "dot files""
        for file in **/.*; do
            echo "Processing $file\n"
            process_file $file
        done
    echo "Done Processing "dot files""

    echo "Renaming main package folder from app_flask_archetype to $target_app_name"
        mv ./src/$current_project_name ./src/$target_app_name
    echo "Done renaming main package folder"

    echo "Removing .env from tracking and adding it to gitignore. You can explicitly add this again for a toy project, should you choose to so."
        git rm --cached .env
        echo ".env" >> .gitignore
    echo "Done"
fi