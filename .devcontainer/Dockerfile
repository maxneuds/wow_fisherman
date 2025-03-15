FROM python:3.12-bookworm

ENV USERNAME=dev
ARG UID
ARG GID
ARG DOCKER_GID

# Setup container user, groups and home
RUN if id -u ${UID} > /dev/null 2>&1; then userdel -f $(getent passwd ${UID} | cut -d: -f1); fi
RUN if getent group ${GID} > /dev/null 2>&1; then groupdel ${GID}; fi
RUN groupadd -g ${UID} ${USERNAME} && \
    useradd -m -u ${GID} -g ${GID} ${USERNAME} && \
    mkdir /workspace && chown ${USERNAME}:${USERNAME} /workspace

# Update repo
RUN apt-get clean && apt-get update

# Make sure locales are set to en_US.UTF-8
RUN apt-get install -y locales && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# <-- PYTHON -->
# Install advanced python build dependencies
RUN apt-get install -y \
    build-essential libssl-dev libffi-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev python3-dev
# Install opencv display dependencies
RUN apt-get install -y \
    libgl1-mesa-glx libx11-dev libwayland-client0 x11-utils qtwayland5
# <-- PYTHON -->

# <- DEVCONTAINER ->
# Enable sudo permissions for container user
RUN apt-get install -y sudo && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# Install zsh and other useful packages
RUN apt-get install -y \
    zsh git wget curl unzip rsync htop vim neofetch
# Install Docker
RUN groupadd -g ${DOCKER_GID} docker
RUN apt-get install -y \
    apt-transport-https ca-certificates curl gnupg lsb-release
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io
# Add container user to docker group
RUN usermod -aG docker ${USERNAME}
# Set up the environment for the container user
RUN chsh -s /bin/zsh ${USERNAME}
# Switch to container user and set home directory
USER ${USERNAME}
# Install oh-my-zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" "" --unattended
# Enable command completion and git support in zsh
RUN git clone https://github.com/zsh-users/zsh-completions ${HOME}/.oh-my-zsh/custom/plugins/zsh-completions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${HOME}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${HOME}/.oh-my-zsh/custom/plugins/zsh-autosuggestions
RUN sed -i 's/plugins=(git)/plugins=(git zsh-completions zsh-syntax-highlighting zsh-autosuggestions)/' ${HOME}/.zshrc
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/' ${HOME}/.zshrc
RUN echo 'prompt_context() {}' >> ${HOME}/.zshrc
# Command alias
RUN echo 'alias ll="ls -lah --color=auto"' >> ${HOME}/.zshrc
RUN echo 'alias cp="rsync -avh --progress"' >> ${HOME}/.zshrc
# Switch back to root user
USER root
# <- DEVCONTAINER ->

# Apt cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch user
USER ${USERNAME}

# Install poetry
RUN pip install poetry
ENV PATH="${HOME}/.local/bin:$PATH"
ENV POETRY_VIRTUALENV_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
